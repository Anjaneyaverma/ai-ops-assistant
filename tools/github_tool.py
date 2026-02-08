import requests

def search_repositories(query: str):
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "sort": "stars", "order": "desc", "per_page": 3}

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()["items"]

    return [
        {
            "name": repo["name"],
            "url": repo["html_url"],
            "stars": repo["stargazers_count"],
            "description": repo["description"]
        }
        for repo in data
    ]
