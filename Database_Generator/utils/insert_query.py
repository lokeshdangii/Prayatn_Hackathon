import mysql.connector
import requests
import json


def generate_insert_query(table_name, col_details):
    # # Making connection
    # connection = mysql.connector.connect(**new_db_config)
    # cursor = connection.cursor()

    # # Extract foreign key details.
    # foreign_key = finding_foreign_key(col_details)
    # print(foreign_key)

    # Construct instruction based on column details
    instruction = f"write insert query with 10 entries and insert real life data that doesn't look generated and looks indian for table {table_name} having columns: {col_details}"

    # Generate insert query instruction using Eden AI
    generated_instruction = generate_instruction_with_eden_ai(instruction)

    # Make request to Eden AI to get the insert query
    insert_query = generate_insert_query_with_eden_ai(generated_instruction)

    # Print the generated query
    print("printing insert query")
    print(insert_query)

    # Return the generated query
    return insert_query


def generate_instruction_with_eden_ai(instruction):
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNGI2MTNlYWQtNjM4Ni00Y2FjLWFlYTctY2QwOTEyODBmZjdhIiwidHlwZSI6ImFwaV90b2tlbiJ9.49f5_0ZfmIbCaYAnjVTUK3mUiVXpmN8UeN4aAARRcss"
    }
    url = "https://api.edenai.run/v1/pretrained/text/generate"
    payload = {
        "text": instruction,
        "model_id": "openai-gpt-3.5-turbo"
    }
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    return result['generated_text']


def generate_insert_query_with_eden_ai(instruction):
    headers = {
        "Authorization": "Bearer <YOUR_EDEN_AI_API_KEY>"
    }
    url = "https://api.edenai.run/v2/text/code_generation"
    payload = {
        "providers": "openai",
        "prompt": "",
        "instruction": instruction,
        "temperature": 0.1,
        "max_tokens": 500,
        "fallback_providers": ""
    }
    response = requests.post(url, headers=headers, json=payload)
    result = json.loads(response.text)
    return result['openai']['generated_text']
