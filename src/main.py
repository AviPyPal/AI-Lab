from src.agents.rag_agent import RAGAgent


def main():
    query = "What is RAG?"

    agent = RAGAgent()
    result = agent.run(query)

    print("\n--- RAG Result ---\n")
    print(result.model_dump())


if __name__ == "__main__":
    main()