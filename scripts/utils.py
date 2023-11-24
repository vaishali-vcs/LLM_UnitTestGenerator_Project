import json
import os
import uuid
from typing import Iterable, Dict
import ast  # used for detecting whether generated Python code is valid
import pandas as pd
import openai


def load_config(config_file: str) -> dict:
    """
    Loads the JSON configuration and sets the OpenAI API key.
    @param config_file:  Path to the JSON configuration file.
    @returns config: dictionary of the parsed configuration
    """
    with open(config_file) as json_file:
        config = json.load(json_file)
    # sets the OpenAI key
    openai.api_key = config["OPEN_AI_KEY"]
    return config


def load_MUT_file(config: dict, MUTs_file: str) -> list:
    """
    Returns a list of prompts used for test generation.
    @param config: analysis configuration
    @param prompt_file:  path to the JSON file containing prompts (ex: "RQ1_Test_Generation/OpenAI_Data/HumanEvalJava_input/original_prompt.json")
    @return: a list of parsed prompts
    """
    return {task["task_id"]: task for task in stream_jsonl(config, MUTs_file)}


def stream_jsonl(config, filename: str) -> Iterable[Dict]:
    file_path = os.path.join(config["BASE_DIRECTORY"], filename)
    with open(file_path, "r") as fp:
        for line in fp:
            if any(not x.isspace() for x in line):
                yield json.loads(line)


def check_code_compilation(code) -> bool:
    try:
        ast.parse(code)
        return True
    except SyntaxError as e:
        print(f"Syntax error in generated code: {e}")
        return False


def get_output_files(config: dict, rq: int, dataset: str, prompt_file: str, max_tokens: int, model: str) -> tuple:
    """
    Compute the paths to the output folder and response file.

    @param rq: research question
    @param dataset: the dataset associated with the prompt file
    @param max_tokens: maximum number of tokens
    @param config: analysis configuration
    @param prompt_file:  path to the JSON file containing prompts (ex: "RQ1_Test_Generation/OpenAI_Data/HumanEvalJava_input/original_prompt.json")
    @param model: the model used for generation (ex: OpenAI, CodeGen)
    @return: a tuple:
    - output_folder: <BASE_DIR>/<RQ_FOLDER>/OpenAI_Data/<DATASET>_output/"
    - scenario_folder: output_folder/<SCENARIO>
    - json_file = output_folder/<SCENARIO>_output_<max_tokens>.json
    - csv_file = output_folder/<SCENARIO>_output_<max_tokens>.csv
    """
    # prompt files are typically named <label>_prompt.json, extract the label part
    scenario_name = os.path.basename(prompt_file).split("_prompt")[0]
    rq_folder = "RQ1_Test_Generation" if rq == 1 else "RQ2_Prompt_Elements"
    output_folder = os.path.join(config["BASE_DIRECTORY"], rq_folder, f"{model}_Data", f"{dataset}_output/")
    scenario_folder = os.path.join(output_folder, scenario_name)
    json_file = os.path.join(output_folder, f"{scenario_name}_output_{max_tokens}.json")
    csv_file = json_file.replace(".json", ".csv")
    return output_folder, scenario_folder, json_file, csv_file


def save_generated_code(output_folder: str, output_file: str, contents: str) -> None:
    """
    Saves the generated Unit Test on a separate file in the output folder.
    @param max_tokens:
    @param prompt: prompt used for test generation.
    @param response: the response returned by OpenAI
    @param output_folder: where to save the Unit Test.
    The file will be named as {response['prompt_id']}Test.xyz (xyz extension is based on the original language of the sample).
    This assumes that the prompt_id is the path to the class under test.
    """

    # create the output folder if needed
    if not os.path.exists(output_folder): os.makedirs(output_folder)

    with open(os.path.join(output_folder,
                           output_file + ".py"), 'w') as generated_testcases:
        generated_testcases.write(contents)


def save_response(output_directory, filename, contents) -> None:
    """
        Saves a response into an open json file
        @param csv_file: an open writeable file where to save the results in CSV format
        @param json_file: an open writeable file where to save the results in JSON format
        @param prompt: the prompt object to be saved
        @param prompts: the list of all prompts (used to check when to stop adding commas)
        @param response: the JSON response object from Codex API to be serialized into the file
        @return: a mock response object with the same structure as the actual response
   """

    df_contents = pd.DataFrame(contents, columns=['Function_ID', 'Status'])
    df_contents.to_csv(os.path.join(output_directory, filename), index=True)


def get_mock_response(prompt: dict, error_msg: str) -> dict:
    """
    Creates a mock response object to be used to record runtime errors
    @param prompt: the prompt object
    @param error_msg: error message to be captured in this mock response
    @return: a mock response object with the same structure as the actual response
    """
    return dict(
        choices=[{
            "finish_reason": "ERROR - " + error_msg,
            "text": ""
        }],
        id=str(uuid.uuid4()),  # generates a dummy ID
        prompt_id=prompt["id"],
        original_code=prompt["original_code"],
        test_prompt=prompt["test_prompt"],
        time_taken=-1,  # dummy
    )


def save_to_dummy_folder(new_code: str, r: dict, suffix: int = 0) -> None:
    """
    Saves the generated code to the dummy_output folder
    @param suffix: a suffix to distinguish between multiple generated code to this function
    @param new_code: code to be saved
    @param r: the response dictionary
    """
    filename = r["prompt_id"][1:].replace("/", "_")
    if suffix > 0: filename = filename.replace(".java", f"_{suffix}.java")
    with open(f"./dummy_output/{filename}", "w") as f:
        f.write(new_code)
