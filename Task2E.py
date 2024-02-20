import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_over_level_threshold
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()

    update_water_levels(stations)
    list = stations_over_level_threshold(stations, 0.0)
    
    for i in range(5):
        station_name = list[i][0]
        for station in stations:
            if station.name == station_name:
                station_object = station
                break
        
        dt = 10
        dates, levels = fetch_measure_levels(
        station_object.measure_id, dt=datetime.timedelta(days=dt))
        
        plot_water_levels(station_object, dates, levels)
    
run()

