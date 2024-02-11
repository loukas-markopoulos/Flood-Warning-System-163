from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest_rel_level_stations = stations_highest_rel_level(stations, 10)

    for i in highest_rel_level_stations:
        print(f'{i[0]} {i[1]}')
        
    return

run()