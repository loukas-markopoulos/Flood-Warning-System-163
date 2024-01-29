from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_over_level_threshold

def run():

    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)

    reversed_sorted_list = stations_over_level_threshold(stations, 0.8)
    for i in reversed_sorted_list:
        print(i[0], i[1])

run()