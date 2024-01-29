from floodsystem.station import MonitoringStation
from .utils import sorted_by_key  # noqa

def stations_over_level_threshold(stations, tol):

    list_over_threshold = []
    for i in stations:
        ratio = MonitoringStation.relative_water_level(i)
        if ratio != "No value":
            if ratio > tol:
                tuple = (i.name, ratio)
                list_over_threshold.append(tuple)
    sorted_list = sorted_by_key(list_over_threshold, 1, True)

    return sorted_list