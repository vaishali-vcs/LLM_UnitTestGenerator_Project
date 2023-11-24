#!/bin/bash

#$ -M x@y.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 1     # Specify parallel environment and legal core size
#$ -q long           # Specify queue
#$ -N  rq2_py_2k_4k

# python generate_tests_codex.py -t 2000 -d HumanEvalPython -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalPython_input/scenario1_prompt.json"
# python generate_tests_codex.py -t 2000 -d HumanEvalPython -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalPython_input/scenario2_prompt.json"
# python generate_tests_codex.py -t 2000 -d HumanEvalPython -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalPython_input/scenario3_prompt.json"

# python generate_tests_codex.py -t 2000 -d HumanEvalPython -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalPython_input/scenario1_prompt.json"
# python generate_tests_codex.py -t 2000 -d HumanEvalPython -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalPython_input/scenario2_prompt.json"
# python generate_tests_codex.py -t 2000 -d HumanEvalPython -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalPython_input/scenario3_prompt.json"


# HumanEvalJava RQ2 (un-comment below)
# python generate_tests_codex.py -t 1000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario1_prompt.json"
# python generate_tests_codex.py -t 1000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario2_prompt.json"
# python generate_tests_codex.py -t 1000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario3_prompt.json"
python generate_tests_openai.py -t 2000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario1_prompt.json"
python generate_tests_openai.py -t 2000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario2_prompt.json"
python generate_tests_openai.py -t 2000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario3_prompt.json"
# python generate_tests_codex.py -t 3000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario1_prompt.json"
# python generate_tests_codex.py -t 3000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario2_prompt.json"
# python generate_tests_codex.py -t 3000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario3_prompt.json"
python generate_tests_openai.py -t 4000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario1_prompt.json"
python generate_tests_openai.py -t 4000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario2_prompt.json"
python generate_tests_openai.py -t 4000 -d HumanEvalJava -q RQ2 -p "RQ2_Prompt_Elements/OpenAI_Data/HumanEvalJava_input/scenario3_prompt.json"
