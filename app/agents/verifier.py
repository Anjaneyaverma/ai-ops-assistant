def verifier_agent(results):
    issues = []
    if "weather" not in results:
        issues.append("Missing weather data")
    if "cafes" not in results:
        issues.append("Missing cafe data")

    return {
        "is_valid": len(issues) == 0,
        "issues": issues
    }
