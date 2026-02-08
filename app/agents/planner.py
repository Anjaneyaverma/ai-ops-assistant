import os
from openai import OpenAI
from app.schemas import Plan

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def planner_agent(user_prompt: str) -> Plan:
    """
    Converts user intent into a structured execution plan.
    No API calls here – only planning.
    """

    response = client.responses.parse(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "You are a Planner Agent. "
                    "Break the user request into clear, ordered steps. "
                    "Do not execute anything. "
                    "Return steps as a JSON array."
                )
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        response_format=Plan
    )

    return response.output_parsed
