# src/rag/retriever.py

def load_documents(file_path: str) -> list:
    with open(file_path, "r") as f:
        content = f.read()

    # Split into simple chunks (by line)
    documents = content.split("\n\n")
    return [doc.strip() for doc in documents if doc.strip()]


def retrieve_relevant_docs(query: str, documents: list) -> list:
    query_words = query.lower().split()

    scored_docs = []

    for doc in documents:
        score = sum(word in doc.lower() for word in query_words)
        if score > 0:
            scored_docs.append((score, doc))

    # Sort by score (highest first)
    scored_docs.sort(reverse=True, key=lambda x: x[0])

    # Return top 2 documents
    return [doc for _, doc in scored_docs[:2]]