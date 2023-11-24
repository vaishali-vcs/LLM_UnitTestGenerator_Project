# imports needed to run the code in this notebook
import ast  # used for detecting whether generated Python code is valid
import os.path
import time
import openai  # used for calling the OpenAI API
import argparse
import pandas as pd

from utils import (
    load_config,
    load_MUT_file,
    check_code_compilation,
    save_generated_code,
    save_response
)

color_prefix_by_role = {
    "system": "\033[0m",  # gray
    "user": "\033[0m",  # gray
    "assistant": "\033[92m",  # green
}


def print_messages(messages, color_prefix_by_role=color_prefix_by_role) -> None:
    """Prints messages sent to or from GPT."""
    for message in messages:
        print(f"{message}")


# example of a function that uses a multi-step prompt to write unit tests
def unit_test_from_function(
        function_to_test: str,  # Python function to test, as a string
        unit_test_package: str = "pytest",  # unit testing package; use the name as it appears in the import statement
        approx_min_cases_to_cover: int = 8,  # minimum number of test case categories to cover (approximate)
        print_text: bool = False,  # optionally prints text; helpful for understanding the function & debugging
        explain_model: str = "gpt-4",  # model used to generate text plans in step 1
        plan_model: str = "gpt-4",  # model used to generate text plans in steps 2 and 2b
        execute_model: str = "gpt-4",  # model used to generate code in step 3
        temperature: float = 0.4,  # temperature = 0 can sometimes get stuck in repetitive loops, so we use 0.4
        reruns_if_fail: int = 2,  # if the output code cannot be parsed, this will re-run the function up to N times
) -> str:
    """Outputs a unit test for a given Python function, using a 3-step GPT-3 prompt."""
    # Step 1: Generate an explanation of the function

    # create a markdown-formatted message that asks GPT to explain the function, formatted as a bullet list
    explain_system_message = {
        "role": "system",
        "content": "You are a world-class Python developer with an eagle eye for unintended bugs and edge cases. You "
                   "carefully explain code with great detail and accuracy. You organize your explanations in "
                   "markdown-formatted, bulleted lists.",
    }
    explain_user_message = {
        "role": "user",
        "content": f"""Please explain the following Python function. Review what each element of the function is 
        doing precisely and what the author's intentions may have been. Organize your explanation as a 
        markdown-formatted, bulleted list.

    ```python
    {function_to_test}
    ```""",
    }
    explain_messages = [explain_system_message, explain_user_message]
    if print_text:
        print_messages(explain_messages)

    explanation_response = openai.chat.completions.create(
        model=explain_model,
        messages=explain_messages,
        temperature=temperature
    )

    explanation = explanation_response.choices[0].message.content

    if print_text:
        print_messages(explanation)

    explain_assistant_message = {"role": "assistant", "content": explanation}

    # introduce delay of 1 minute before the next API Call
    time.sleep(60)

    # Step 2: Generate a plan to write a unit test

    # Asks GPT to plan out cases the units tests should cover, formatted as a bullet list
    plan_user_message = {
        "role": "user",
        "content": f"""A good unit test suite should aim to:
    - Test the function's behavior for a wide range of possible inputs
    - Test edge cases that the author may not have foreseen
    - Take advantage of the features of `{unit_test_package}` to make the tests easy to write and maintain
    - Be easy to read and understand, with clean code and descriptive names
    - Be deterministic, so that the tests always pass or fail in the same way

    To help unit test the function above, list diverse scenarios that the function should be able to handle (and under each scenario, include a few examples as sub-bullets).""",
    }
    plan_messages = [
        explain_system_message,
        explain_user_message,
        explain_assistant_message,
        plan_user_message,
    ]
    if print_text:
        print_messages([plan_user_message])
    plan_response = openai.chat.completions.create(
        model=plan_model,
        messages=plan_messages,
        temperature=temperature
    )

    plan = plan_response.choices[0].message.content

    if print_text:
        print_messages(plan)

    plan_assistant_message = {"role": "assistant", "content": plan}

    # introduce delay of 1 minute before the next API Call
    time.sleep(60)

    # Step 2b: If the plan is short, ask GPT to elaborate further
    # this counts top-level bullets (e.g., categories), but not sub-bullets (e.g., test cases)
    num_bullets = plan.count("\n\n")
    elaboration_needed = num_bullets < approx_min_cases_to_cover
    if elaboration_needed:
        elaboration_user_message = {
            "role": "user",
            "content": f"""In addition to those scenarios above, list a few rare or unexpected edge cases (and as 
            before, under each edge case, include a few examples as sub-bullets).""",
        }
        elaboration_messages = [
            explain_system_message,
            explain_user_message,
            explain_assistant_message,
            plan_user_message,
            plan_assistant_message,
            elaboration_user_message,
        ]
        if print_text:
            print_messages([elaboration_user_message])
        elaboration_response = openai.chat.completions.create(
            model=plan_model,
            messages=elaboration_messages,
            temperature=temperature
        )

        elaboration = explanation_response.choices[0].message.content

        if print_text:
            print_messages(elaboration)

        elaboration = elaboration_response.choices[0].message.content
        elaboration_assistant_message = {"role": "assistant", "content": elaboration}

    # introduce delay of 1 minute before the next API Call
    time.sleep(60)

    # Step 3: Generate the unit test

    # create a markdown-formatted prompt that asks GPT to complete a unit test
    package_comment = ""
    if unit_test_package == "pytest":
        package_comment = ("# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize "
                           "decorator")
    execute_system_message = {
        "role": "system",
        "content": "You are a world-class Python developer with an eagle eye for unintended bugs and edge cases. You "
                   "write careful, accurate unit tests. When asked to reply only with code, you write all of your "
                   "code in a single block.",
    }
    execute_user_message = {
        "role": "user",
        "content": f"""Using Python and the `{unit_test_package}` package, write a suite of unit tests for the 
        function, following the cases above. Include helpful comments to explain each line. Reply only with code, 
        formatted as follows:

    ```python
    # imports
    import {unit_test_package}  # used for our unit tests
    {{insert other imports as needed}}

    # function to test
    {function_to_test}

    # unit tests
    {package_comment}
    {{insert unit test code here}}
    ```""",
    }
    execute_messages = [
        execute_system_message,
        explain_user_message,
        explain_assistant_message,
        plan_user_message,
        plan_assistant_message,
    ]
    if elaboration_needed:
        execute_messages += [elaboration_user_message, elaboration_assistant_message]
    execute_messages += [execute_user_message]
    if print_text:
        print_messages([execute_system_message, execute_user_message])

    execute_response = openai.chat.completions.create(
        model=execute_model,
        messages=execute_messages,
        temperature=temperature
    )
    execution = ""
    execution = execute_response.choices[0].message.content

    # check the output for errors
    code = execution.split("```python")[1].split("```")[0].strip()
    try:
        ast.parse(code)
    except SyntaxError as e:
        print(f"Syntax error in generated code: {e}")
        if reruns_if_fail > 0:
            print("Rerunning...")
            return unit_test_from_function(
                function_to_test=function_to_test,
                unit_test_package=unit_test_package,
                approx_min_cases_to_cover=approx_min_cases_to_cover,
                print_text=print_text,
                explain_model=explain_model,
                plan_model=plan_model,
                execute_model=execute_model,
                temperature=temperature,
                reruns_if_fail=reruns_if_fail - 1,  # decrement rerun counter when calling again
            )

    # return the unit test as a string
    return code


def main():
    generation_status = []

    example_function = """def pig_latin(text):
        def translate(word):
            vowels = 'aeiou'
            if word[0] in vowels:
                return word + 'way'
            else:
                consonants = ''
                for letter in word:
                    if letter not in vowels:
                        consonants += letter
                    else:
                        break
                return word[len(consonants):] + consonants + 'ay'

        words = text.lower().split()
        translated_words = [translate(word) for word in words]
        return ' '.join(translated_words)
    """

    config = load_config("config.json")

    python_methods = load_MUT_file(config, os.path.join(config["INPUT_DIRECTORY"], "python_functions.jsonl"))

    for task_id in python_methods.keys():
        status_item = [python_methods[task_id]['task_id']]
        question_text = python_methods[task_id]['question']
        if check_code_compilation(question_text):
            print(f"{task_id} Pass ")

            if python_methods[task_id]['generate'] == 'yes':
                code = unit_test_from_function(question_text, approx_min_cases_to_cover=10, print_text=True)
                status_item.append('Pass')

                save_generated_code(os.path.join(config["BASE_DIRECTORY"], config["OUTPUT_DIRECTORY"]),
                                    python_methods[task_id]['task_id'], code)

        generation_status.append(status_item)

    save_response(os.path.join(config["BASE_DIRECTORY"], config["OUTPUT_DIRECTORY"]),
                  "generation_status.csv", generation_status)
    # Create the pandas DataFrame


if __name__ == "__main__":
    main()
