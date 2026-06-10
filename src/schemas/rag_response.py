from pydantic import BaseModel
from typing import List


class RAGResponse(BaseModel):
    query: str
    context_used: List[str]
    answer: str
