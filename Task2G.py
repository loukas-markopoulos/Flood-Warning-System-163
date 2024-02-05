from floodsystem.finalprogramme import  danger_lists, list_of_towns, final_print
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)


    seperate_lists_of_stations_list = danger_lists(stations)
    seperate_lists_of_towns_list = list_of_towns(seperate_lists_of_stations_list)
    final_print(seperate_lists_of_towns_list)

    return

run()