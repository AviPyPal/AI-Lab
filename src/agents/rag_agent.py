from src.rag.retriever import load_documents, retrieve_relevant_docs
from src.schemas.rag_response import RAGResponse


class RAGAgent:
    def run(self, query: str) -> RAGResponse:
        print("\n--- RAG Agent ---\n")

        documents = load_documents("datasets/knowledge.txt")
        relevant_docs = retrieve_relevant_docs(query, documents)

        context = "\n\n".join(relevant_docs)

        print("Retrieved Context:")
        print(context)

        return RAGResponse(
            query=query,
            context_used=relevant_docs,
            answer="This is a simulated grounded response based on retrieved context."
        )