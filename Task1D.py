from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():

    length = len(rivers_with_station(stations))
    ordered_rivers = rivers_with_station.sort()
    print(f'{length} stations. First 10 - {ordered_rivers[:10]}')

    print(f'{stations_on_river['River Aire']'})
    print(f'{stations_on_river['River Cam']'})
    print(f'{stations_on_river['River Thames']'})

run()