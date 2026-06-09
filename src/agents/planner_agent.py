class PlannerAgent:
    def plan(self, user_input: str) -> str:
        print("\n--- Planner Agent ---\n")
        print(f"Received input: {user_input}")

        # Simple rule-based planning (we don't use LLM yet)
        if "summarize" in user_input.lower():
            return "summarize"

        return "unknown"