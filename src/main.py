from utils.printer import print_message
from prompts.basic_prompt import create_summary_prompt
from prompts.structured_prompt import create_structured_summary_prompt
from utils.parser import parse_summary_response



def main():
    print("AI Lab is set up successfully.")
    print("You are now building like a professional AI engineer.")

    print_message()
    sample_text = "AI engineering involves building scalable systems using machine learning models, APIs, and structured workflows."
    prompt = create_summary_prompt(sample_text)

    print("\n--- Generated Prompt ---\n")
    print(prompt)

    
# Simulated LLM response
    simulated_response = """
    {
      "summary": [
        "AI engineering focuses on scalable system design",
        "It uses machine learning models and APIs",
        "Structured workflows are essential"
      ]
    }
    """

    parsed = parse_summary_response(simulated_response)

    print("\n--- Parsed Output ---\n")
    print(parsed)


if __name__ == "__main__":
    main()  