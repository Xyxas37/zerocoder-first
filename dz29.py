import requests
import pprint

url = "https://api.github.com/search/repositories"

params = {
    "q": "language:html",
}
response = requests.get(url, params=params)

print(response.status_code)
response_json = response.json()
pprint.pprint(response_json)
