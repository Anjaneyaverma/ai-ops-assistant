from fastapi import FastAPI
from app.agents.planner import planner_agent
from app.agents.executor import executor_agent
from app.agents.verifier import verifier_agent

app = FastAPI()

@app.post("/run")
def run_agent(prompt: str):
    plan = planner_agent(prompt)
    results = executor_agent(plan)
    verification = verifier_agent(results)

    return {
        "plan": plan,
        "results": results,
        "verification": verification
    }
