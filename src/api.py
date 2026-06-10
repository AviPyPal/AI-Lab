from fastapi import FastAPI
from src.agents.planner_agent import PlannerAgent
from src.agents.summary_agent import SummaryAgent
from src.agents.rag_agent import RAGAgent

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Lab API is running"}


@app.get("/summarize")
def summarize(query: str):
    planner = PlannerAgent()
    task = planner.plan(f"Summarize {query}")

    if task == "summarize":
        agent = SummaryAgent()
        result = agent.execute(query)
        return result

    return {"error": "No suitable agent found"}


@app.get("/rag")
def rag(query: str):
    agent = RAGAgent()
    result = agent.run(query)
    return result.model_dump()