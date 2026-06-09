from prompts.structured_prompt import create_structured_summary_prompt
from utils.parser import parse_summary_response


class SummaryAgent:
    def execute(self, text: str) -> dict:
        prompt = create_structured_summary_prompt(text)

        print("\n--- Summary Agent (Executor) ---\n")
        print(prompt)

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
