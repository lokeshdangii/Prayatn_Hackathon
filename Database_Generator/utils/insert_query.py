import requests
import json
import re

# Load API keys from a JSON configuration file
with open("config.json") as f:
    config = json.load(f)

openai_api_key = config["openai_api_key"]


def generate_insert_query(table_name, col_details):
    headers = {"Authorization": f"Bearer {openai_api_key}"}

    instruction = f"write insert query with real life data that doesn't seem generated and looks indian 10 entries for table {table_name} having columns: {col_details} Also make sure that size of each entry for all columns should be strictly according to the size given in round bracket after datatype"

    url = "https://api.edenai.run/v2/text/code_generation"
    payload = {
        "providers": "openai",
        "prompt": "",
        "instruction": instruction,
        "temperature": 0.1,
        "max_tokens": 500,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)

    print(result)

    generated_text = result['openai']['generated_text']

    # Construct instruction based on column details

    # Generate insert query instruction using OpenAI's GPT
    # generated_instruction = generate_instruction_with_openai_gpt(instruction)

    # Make request to OpenAI to get the insert query
    sql_query_start_index = generated_text.find("INSERT INTO")
    sql_query = generated_text[sql_query_start_index:]
    # insert_query = generate_insert_query_with_openai_gpt(generated_instruction
    end_index = sql_query.find("```")
    sql_query = sql_query[:end_index]

    # Check if the character before "```" is a semicolon, if not, add a semicolon
    if not re.search(r';```', sql_query):
        semicolon_index = sql_query.rfind(';')
        if semicolon_index == -1:
            semicolon_index = 0
        sql_query = sql_query[:semicolon_index] + \
            ';' + sql_query[semicolon_index:]

    return sql_query
