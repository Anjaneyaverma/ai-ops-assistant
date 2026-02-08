from app.tools.weather import get_weather
from app.tools.places import get_places

def executor_agent(plan):
    results = {}
    for step in plan.steps:
        if "weather" in step.lower():
            results["weather"] = get_weather("Bangalore")
        if "cafe" in step.lower():
            results["cafes"] = get_places("cafes")
    return results
