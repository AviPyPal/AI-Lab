# src/prompts/structured_prompt.py

def create_structured_summary_prompt(text: str) -> str:
    prompt = f"""
You are an expert assistant.

Your task is to summarize the input text.

Return the output in the following JSON format:

{{
  "summary": [
    "point 1",
    "point 2",
    "point 3"
  ]
}}

Text:
{text}
"""
    return prompt.strip()
