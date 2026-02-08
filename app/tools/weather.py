import requests, os

def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": os.getenv("WEATHER_API_KEY"),
        "units": "metric"
    }
    return requests.get(url, params=params).json()
