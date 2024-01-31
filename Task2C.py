from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()

    return stations_highest_rel_level(stations, 10)

run()