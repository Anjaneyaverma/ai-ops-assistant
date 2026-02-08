import json
from llm.client import call_llm

SYSTEM_PROMPT = """
You are a Planner Agent.
Convert user requests into a JSON execution plan.
Only return valid JSON.
"""

def create_plan(user_task: str):
    prompt = f"""
Create a step-by-step plan for this task:

"{user_task}"

Available tools:
- github_search(query)
- get_weather(city)

Return JSON in this format:
{{
  "steps": [
    {{
      "tool": "github_search",
      "query": "example"
    }},
    {{
      "tool": "get_weather",
      "city": "example"
    }}
  ]
}}
"""
    response = call_llm(SYSTEM_PROMPT, prompt)
    return json.loads(response)
