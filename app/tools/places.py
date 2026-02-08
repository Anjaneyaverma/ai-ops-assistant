import requests, os

def get_places(query: str, location="Bangalore"):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"{query} in {location}",
        "key": os.getenv("GOOGLE_PLACES_API_KEY")
    }
    return requests.get(url, params=params).json()
