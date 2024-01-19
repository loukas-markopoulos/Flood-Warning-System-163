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