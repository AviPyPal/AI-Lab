from src.agents.planner_agent import PlannerAgent
from src.agents.summary_agent import SummaryAgent


def main():
    user_input = "Summarize AI engineering concepts"

    planner = PlannerAgent()
    task = planner.plan(user_input)

    if task == "summarize":
        executor = SummaryAgent()
        result = executor.execute(user_input)

        print("\n--- Final Result ---\n")
        print(result)
    else:
        print("No suitable agent found.")


if __name__ == "__main__":
    main()