# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


# C
def stations_within_radius(stations, centre, r):
    close_stations = []
    for i in stations:
        if haversine(centre, i.coord) < r:
            close_stations.append(i.name)
    close_stations.sort()
    return close_stations


# B
def stations_by_distance(stations, p):

    station_distance = []

    for i in stations:
        d = haversine(i.coord, p)
        tuple = (i.name, i.town, d)
        station_distance.append(tuple)

    return sorted_by_key(station_distance, 2)


# D
def rivers_with_station(stations):
    rivers = set()

    for i in stations:
        rivers.add(i.river)
    
    rivers_list = list(rivers)
    return rivers_list


def stations_by_river(stations):

    stations_on_river = {}
    rivers = rivers_with_station(stations)

    for i in range(len(rivers)):
        station_list = []
        for j in stations:
            if j.river == rivers[i]:
                station_list.append(j.name)

        ordered_station_list = sorted(station_list)
        stations_on_river[rivers[i]] = ordered_station_list
        
    return stations_on_river


