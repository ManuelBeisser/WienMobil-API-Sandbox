import json
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# FIX: capacity is only calculated for those that have it! so no 100% of stations!


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
    return results


def calculate_availability(data: list) -> dict:
    results = dict()

    for entry in data:
        for time, stations in entry.items():
            timestamp_availability = int()
            time_converted = datetime.strptime(time, "%d/%m/%Y - %H:%M")

            for name, station_data in stations.items():
                timestamp_availability += station_data["avail_bikes"]
            results[time_converted] = timestamp_availability

    return results


def main():
    data = data_import("output.json")
    capacity_data = calculate_capacity(data)
    availability_data = calculate_availability(data)

    # plot pie chart
    fig, ax = plt.subplots()
    ax.pie(capacity_data, labels=["Over Capacity", "At Capacity", "Under Capacity"], colors=["red", "yellow", "green"])
    plt.savefig("capacity_pie.png")

    # plot availability
    x_coordinates = list()
    y_coordinates = list()

    for x, y in availability_data.items():
        x_coordinates.append(x)
        y_coordinates.append(y)

    fig, ax = plt.subplots()
    ax.plot(x_coordinates, y_coordinates, "o-g")
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    plt.savefig("availability.png")


if __name__ == "__main__":
    main()
