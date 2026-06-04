# src/utils/parser.py

import json


def parse_summary_response(response: str) -> dict:
    try:
        data = json.loads(response)
        return data
    except json.JSONDecodeError:
        print("Failed to parse JSON response.")
        return {}   