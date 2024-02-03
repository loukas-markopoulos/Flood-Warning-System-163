# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


# 1C
# returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x
def stations_within_radius(stations, centre, r):

    close_stations = []

    for i in stations:
        if haversine(centre, i.coord) < r:
            close_stations.append(i.name)
    close_stations.sort()

    return close_stations


# 1B
def stations_by_distance(stations, p):

    station_distance = []

    for i in stations:
        d = haversine(i.coord, p)
        tuple = (i.name, i.town, d)
        station_distance.append(tuple)

    return sorted_by_key(station_distance, 2)


# 1D
def rivers_with_station(stations):
    rivers = set()

    for i in stations:
        rivers.add(i.river)
    
    rivers_list = list(rivers)
    rivers_list.sort()
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


# 1E
def rivers_by_station_number(stations, N):
    #create list for tuples
    #create tuple of (dictionary key, length of dictionary value)
    #add tuple to list
    #order list using function from before

    stations_on_river = stations_by_river(stations)

    river_statnumber = []

    for river in stations_on_river:
        tuple = (river, len(stations_on_river[river]))
        river_statnumber.append(tuple)
    
    sorted_river_statnumber = sorted_by_key(river_statnumber, 1)

    i = 1
    while sorted_river_statnumber[-N][1] == sorted_river_statnumber[-(N + i)][1]:
        i += 1

    final_list = []

    for j in range(N + i - 1):
        final_list.append(sorted_river_statnumber[- j - 1])
    
    print(f'{final_list}')
