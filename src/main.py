from agents.summary_agent import SummaryAgent


def main():
    text = "AI engineering involves building scalable systems using machine learning models, APIs, and structured workflows."

    agent = SummaryAgent()
    result = agent.run(text)

    print("\n--- Agent Result ---\n")
    print(result)


if __name__ == "__main__":
    main()