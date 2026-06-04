from utils.printer import print_message
from prompts.basic_prompt import create_summary_prompt


def main():
    print("AI Lab is set up successfully.")
    print("You are now building like a professional AI engineer.")

    print_message()
    sample_text = "AI engineering involves building scalable systems using machine learning models, APIs, and structured workflows."
    prompt = create_summary_prompt(sample_text)

    print("\n--- Generated Prompt ---\n")
    print(prompt)

if __name__ == "__main__":
    main()  