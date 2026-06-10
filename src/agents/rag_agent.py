from src.rag.retriever import load_documents, retrieve_relevant_docs


class RAGAgent:
    def run(self, query: str) -> dict:
        print("\n--- RAG Agent ---\n")

        documents = load_documents("datasets/knowledge.txt")

        relevant_docs = retrieve_relevant_docs(query, documents)

        context = "\n\n".join(relevant_docs)

        print("Retrieved Context:")
        print(context)

        # Simulated structured response
        return {
            "query": query,
            "context_used": relevant_docs,
            "answer": "This is a simulated grounded response based on retrieved context."
        }