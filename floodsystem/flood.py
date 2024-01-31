from floodsystem.station import MonitoringStation
from .utils import sorted_by_key  # noqa

#2B
def stations_over_level_threshold(stations, tol):

    list_over_threshold = []
    for i in stations:
        ratio = MonitoringStation.relative_water_level(i)
        if ratio != None:
            if ratio > tol:
                tuple = (i.name, ratio)
                list_over_threshold.append(tuple)
    sorted_list = sorted_by_key(list_over_threshold, 1, True)

    return sorted_list

# 2C

def stations_highest_rel_level(stations, N):
    sorted_list = stations_over_level_threshold(stations, 0.0)
    for i in range(N):
        print(f'{sorted_list[i][0]} {sorted_list[i][1]}')
    

