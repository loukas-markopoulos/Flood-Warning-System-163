from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    ordered_stations = stations_by_distance(stations, (52.2053, 0.1218))
    print(ordered_stations[:10])
    print(ordered_stations[-10:])
    
    return

run()