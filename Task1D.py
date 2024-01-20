from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list 

def run():

    stations = build_station_list()

    print(f'{len(rivers_with_station(stations))} stations. First 10 - {rivers[:10]}')


    stations_on_river = stations_by_river(stations)

    print(f'{stations_on_river["River Aire"]}')
    print(f'{stations_on_river["River Cam"]}')
    print(f'{stations_on_river["River Thames"]}')

run()