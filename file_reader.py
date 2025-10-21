import pandas as pd
import requests

# TODO: combine names and stations
# TODO: write output function

def fetcher(url: str) -> dict:
    response = requests.get(url)
    return response.json()

def status_cleaner(status: dict) -> dict:
    stations = status["data"]["stations"]
    station_dict = dict()
    for station in stations:
        station_id = station.get("station_id")  # str
        avail_bikes = station.get("num_bikes_available")  # int
        rent_status = station.get("is_renting")  # bool
        return_status = station.get("is_returning")  # bool

        station_id_dict = {
                "avail_bikes": avail_bikes,
                "rent_status": rent_status,
                "return_status": return_status
        }
        station_dict[station_id] = station_id_dict
    return station_dict


if __name__ == "__main__":
    status = fetcher("https://api.wstw.at/gateway/WL_WIENMOBIL_API/1/station_status.json")
    information = fetcher("https://api.wstw.at/gateway/WL_WIENMOBIL_API/1/station_information.json")

    print(status_cleaner(status))
    print(len(status_cleaner(status)))
