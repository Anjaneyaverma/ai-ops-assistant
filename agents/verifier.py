def verify_and_format(results: list):
    final_output = {}

    for item in results:
        final_output.update(item)

    return {
        "status": "success",
        "data": final_output
    }
