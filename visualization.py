import json

import matplotlib.pyplot as plt

# TODO: make pie plot of the amount of stations over capacity
# TODO: make plot of the last 24hrs avail. bikes


def data_import(text_file: str) -> list:
    json_data = open(text_file)
    data = json.load(json_data)
    json_data.close()
    return data


def calculate_overcapacity(data: list) -> list:
    over_capacity_counter = int()
    at_capacity_counter = int()
    under_capacity_counter = int()
    over_capacity_list = list()

    last_timestamp = data[-1]
    for time, stations in last_timestamp.items():
        for name, station_data in stations.items():
            station_cap = station_data["station_capacity"]
            station_bikes = station_data["avail_bikes"]

            if station_cap is None:
                pass
            elif station_bikes == station_cap:
                at_capacity_counter += 1
            elif station_bikes < station_cap:
                under_capacity_counter += 1
            else:
                over_capacity_counter += 1
                over_capacity_list.append(name)

    results = [over_capacity_counter, at_capacity_counter, under_capacity_counter]
    print(over_capacity_list)
    return results


def main():
    data = data_import("output.json")
    print(calculate_overcapacity(data))


if __name__ == "__main__":
    main()
