import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_over_level_threshold
from floodsystem.analysis import polyfit

def run():
    
    stations = build_station_list()

    update_water_levels(stations)
    list = stations_over_level_threshold(stations, 0.0)
    
    for i in range(1):
        station_name = list[i][0]
        for station in stations:
            if station.name == station_name:
                station_object = station
                break
        
        dt = 2
        dates, levels = fetch_measure_levels(station_object.measure_id, dt=datetime.timedelta(days=dt))
        
        
        polyfit(dates, levels, 5)
        print(f'{polyfit(dates, levels, 5)[0]}')
        print(f'{polyfit(dates, levels, 5)[0].deriv()}')
        print(f'{polyfit(dates, levels, 5)[0].deriv()(1)}')
    return

run()