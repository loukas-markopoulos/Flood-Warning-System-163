from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    stations = build_station_list()

    return print(rivers_by_station_number(stations, 9))

run()

