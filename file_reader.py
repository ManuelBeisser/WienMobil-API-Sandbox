import requests


def fetcher(url: str):
    response = requests.get(url)
    return response.json()

api_url = "https://api.wstw.at/gateway/WL_WIENMOBIL_API/1/station_status.json"
print(fetcher(api_url))
