from fastapi import FastAPI
from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify_and_format
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/run")
def run_task(payload: dict):
    user_task = payload.get("task")

    plan = create_plan(user_task)
    execution_results = execute_plan(plan)
    final_response = verify_and_format(execution_results)

    return final_response
