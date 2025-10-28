import json

import matplotlib.pyplot as plt

# FIX: capacity is only calculated for those that have it! so no 100% of stations!
# TODO: make plot of the last 24hrs avail. bikes


def data_import(text_file: str) -> list:
    json_data = open(text_file)
    data = json.load(json_data)
    json_data.close()
    return data


def calculate_capacity(data: list) -> list:
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


def calculate_availability(data: list):
    results = dict()
    for entry in data:
        for time, stations in entry.items():
            timestamp_availability = int()
            for name, station_data in stations.items():
                timestamp_availability += station_data["avail_bikes"]
            results[time] = timestamp_availability
    return results


def main():
    data = data_import("output.json")

    capacity_data = calculate_capacity(data)

    print(calculate_availability(data))

    # plot pie chart
    fig, ax = plt.subplots()
    ax.pie(capacity_data, labels=["Over Capacity", "At Capacity", "Under Capacity"], colors=["red", "yellow", "green"])
    plt.savefig("capacity_pie.png")


if __name__ == "__main__":
    main()
