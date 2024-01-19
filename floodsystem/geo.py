# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_within_radius(stations, centre, r):
    close_stations = []
    for i in stations:
        if haversine(centre, i.coord) < r:
            close_stations.append(i.name)
    close_stations.sort()
    return close_stations

def stations_by_distance(stations, p):
     #create list
    station_distance = []


    #calculate distance of stations in station(MonitoringStation) to p
    #create tuple of (station(MonitoringStation), distance)
    #append tuple to the station_distance list
    #utils.sort_by_key


    for i in stations:
        d = haversine(i.coord, p)
        tuple = (i.name, i.town, d)
        station_distance.append(tuple)


    return sorted_by_key(station_distance, 2)