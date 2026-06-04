# src/prompts/basic_prompt.py

def create_summary_prompt(text: str) -> str:
    prompt = f"""
You are an expert assistant.

Your task is to summarize the following text clearly and concisely.

Text:
{text}

Return the summary in 3 bullet points.
"""
    return prompt.strip()