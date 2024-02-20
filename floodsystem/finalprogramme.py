import datetime

from floodsystem.analysis import polyfit
from matplotlib.dates import date2num
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_over_level_threshold
import numpy as np
import math as math

#function returning the gradient and second differential- include approximation for 0
def gradient_and_second_deriv(levels, dates, p):

    if polyfit(dates, levels, p)[0] != None and polyfit(dates, levels, p)[1] != None:

        water_level_plot, d0 = polyfit(dates, levels, p)

        x = date2num(dates)

        indicies = []
        for i in range(len(x)):
            if math.isnan(x[i]) == True:
                indicies.append(i) 
        x = np.delete(x, indicies)

        recent_date = x[0] - d0
        # print(f'recent date: {recent_date}')

        gradient_function = water_level_plot.deriv()
        grad = gradient_function(recent_date) 

        # threshold 0 gradient value is set to 0 here
        if abs(grad) < 0.1:
            grad = 0

        second_differential_function = gradient_function.deriv()
        second_differential = second_differential_function(recent_date)

        # threshold 0 second differential value is set to 0 here
        if abs(second_differential) < 0.1:
            second_differential = 0
        
        # print(f'grad and second diff: {grad}, {second_differential}')
        
        data = [grad, second_differential]

        return data
    
    else:
        return


#function returning a tuple of (X, Y, Z) for each station 
def X_Y_Z(station):

    if MonitoringStation.typical_range_consistent(station) is True:
        X = (station.typical_range[1]) * 0.8 #determine value for X
        Y = (station.typical_range[1]) * 2.0 #determine value for Y 
        Z = (station.typical_range[1]) * 3.0 #determine value for Z
        threshold_values = [X, Y, Z]
    else:
        threshold_values = [None, None, None]

    # print(f'threshold values: {station.typical_range[1]}, {X}, {Y}, {Z}')

    return threshold_values

#function sorting a station to an appropriate list 
def append_station_to_list(recent_level, grad, second_differential, X, Y, Z, rel_high, station, severe_list, high_list, medium_list, low_list):
    if recent_level >= Z:
        if grad > 0 or grad == 0:
            severe_list.append(station)
            return

        elif grad < 0 and second_differential < 0:
            severe_list.append(station)
            return

        else:
            high_list.append(station)
            return
            
    if recent_level >= Y and recent_level < Z:
        if grad > 0:
            severe_list.append(station)
            return
            
        elif grad == 0 and second_differential > 0:
            severe_list.append(station)
            return
            
        elif grad == 0 and second_differential == 0:
            severe_list.append(station)
            return
            
        elif grad == 0 and second_differential < 0:
            high_list.append(station)
            return
            
        elif grad < 0 and second_differential > 0:
            medium_list.append(station)
            return
            
        elif grad < 0 and second_differential == 0:
            medium_list.append(station)
            return
            
        elif grad < 0 and second_differential < 0:
            high_list.append(station)
            return
        
    if recent_level >= rel_high and recent_level < Y:
        if grad < 0:
            medium_list.append(station)
            return
            
        elif grad > 0 and second_differential > 0:
            high_list.append(station)
            return
            
        elif grad > 0 and second_differential == 0:
            high_list.append(station)
            return

        elif grad > 0 and second_differential < 0:
            medium_list.append(station)
            return
            
        elif grad == 0 and second_differential > 0:
            high_list.append(station)
            return
            
        elif grad == 0 and second_differential == 0:
            high_list.append(station)
            return

        elif grad == 0 and second_differential < 0:
            medium_list.append(station)
            return
        
    if recent_level >= X and recent_level < rel_high:
        if grad < 0:
            low_list.append(station)
            return
            
        elif grad > 0 and second_differential > 0:
            medium_list.append(station)
            return

        elif grad > 0 and second_differential == 0:
            medium_list.append(station)
            return

        elif grad > 0 and second_differential < 0:
            low_list.append(station)
            return
            
        elif grad == 0 and second_differential > 0:
              medium_list.append(station)
              return
            
        elif grad == 0 and second_differential == 0:
             medium_list.append(station)
             return
            
        elif grad == 0 and second_differential < 0:
            low_list.append(station)
            return
        
    else:
        low_list.append(station)
        return

#function creating the list of stations for S, H, M, L 
def danger_lists(stations):
    
    severe_list = []
    high_list = []
    medium_list = []
    low_list = []

    N = 5 # number of stations analysed 

    list_of_stations = stations_over_level_threshold(stations, 0.0)

    for i in range(N):
        station_name = list_of_stations[i][0]
        for station in stations:
                if station.name == station_name:
                    station_object = station
                    break
            
        dt = 10 # eg dt=5.over the past 5 days 

        dates, levels = fetch_measure_levels(
        station_object.measure_id, dt=datetime.timedelta(days=dt))

        if len(levels) != 0 and MonitoringStation.typical_range_consistent(station_object) is True:
            recent_level = levels[0]

            # print(f'{recent_level}')

            grad = (gradient_and_second_deriv(levels, dates, 5))[0]
            second_differential = (gradient_and_second_deriv(levels, dates, 5))[1]


            rel_high = station.typical_range[1]
            X = X_Y_Z(station_object)[0]
            Y = X_Y_Z(station_object)[1]
            Z = X_Y_Z(station_object)[2]

            append_station_to_list(recent_level, grad, second_differential, X, Y, Z, rel_high, station_object, severe_list, high_list, medium_list, low_list)
        else:
            break

    seperate_lists_of_stations_list = []
    seperate_lists_of_stations_list.append(severe_list)
    seperate_lists_of_stations_list.append(high_list)
    seperate_lists_of_stations_list.append(medium_list)
    seperate_lists_of_stations_list.append(low_list)

    return seperate_lists_of_stations_list

def list_of_towns(seperate_lists_of_stations_list):

    severe_towns = []
    high_towns = []
    medium_towns = []
    low_towns = []

    if seperate_lists_of_stations_list[0] != []:
        for station in seperate_lists_of_stations_list[0]:
            severe_towns.append(station.town)

    if seperate_lists_of_stations_list[1] != []:
        for station in seperate_lists_of_stations_list[1]:
            high_towns.append(station.town)

    if seperate_lists_of_stations_list[2] != []:
        for station in seperate_lists_of_stations_list[2]:
            medium_towns.append(station.town)

    if seperate_lists_of_stations_list[3] != []:
        for station in seperate_lists_of_stations_list[3]:
            low_towns.append(station.town)
    
    seperate_lists_of_towns_list = []
    seperate_lists_of_towns_list.append(severe_towns)
    seperate_lists_of_towns_list.append(high_towns)
    seperate_lists_of_towns_list.append(medium_towns)
    seperate_lists_of_towns_list.append(low_towns)

    return seperate_lists_of_towns_list

#function printing the seperate lists
def final_print(seperate_lists_of_towns_list):

    if len(seperate_lists_of_towns_list[0]) == 0:
        print('No towns are at severe risk.')
    else:
        print('Towns at severe risk are:')
        for i in seperate_lists_of_towns_list[0]:
            print(f'{i}')
    
    if len(seperate_lists_of_towns_list[1]) == 0:
        print('No towns are at high risk.')
    else:
        print('Towns at high risk are:')
        for i in seperate_lists_of_towns_list[1]:
            print(f'{i}')
    
    if len(seperate_lists_of_towns_list[2]) == 0:
        print('No towns are at medium risk.')
    else:
        print('Towns at medium risk are:')
        for i in seperate_lists_of_towns_list[2]:
            print(f'{i}')

    if len(seperate_lists_of_towns_list[3]) == 0:
        print('No towns are at low risk.')
    else:
        print('Towns at low risk are:')
        for i in seperate_lists_of_towns_list[3]:
            print(f'{i}')
    
    