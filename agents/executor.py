from tools.github_tool import search_repositories
from tools.weather_tool import get_weather

def execute_plan(plan: dict):
    results = []

    for step in plan["steps"]:
        if step["tool"] == "github_search":
            result = search_repositories(step["query"])
            results.append({"github_results": result})

        elif step["tool"] == "get_weather":
            result = get_weather(step["city"])
            results.append({"weather": result})

    return results
