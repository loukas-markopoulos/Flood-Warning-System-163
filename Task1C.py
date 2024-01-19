from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    return print(stations_within_radius(stations, (52.2053, 0.1218), 10))

run()