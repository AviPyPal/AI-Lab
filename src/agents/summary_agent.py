from prompts.structured_prompt import create_structured_summary_prompt
from utils.parser import parse_summary_response


class SummaryAgent:
    def run(self, text: str) -> dict:
        prompt = create_structured_summary_prompt(text)

        print("\n--- Agent Prompt ---\n")
        print(prompt)

        # Simulated LLM response (no API yet)
        simulated_response = """
        {
          "summary": [
            "AI engineering focuses on scalable system design",
            "It uses machine learning models and APIs",
            "Structured workflows are essential"
          ]
        }
        """

        parsed_output = parse_summary_response(simulated_response)
        return parsed_output
