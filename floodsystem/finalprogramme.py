import datetime

from floodsystem.analysis import polyfit
from matplotlib.dates import date2num
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import typical_range_consistent

#function returning the gradient and second differential- include approximation for 0
def gradient_and_second_deriv(levels, dates, p):
    numdates = date2num(dates)

    water_level_plot = polyfit(dates, levels, p)[0]

    gradient_function = water_level_plot.deriv()
    grad = gradient_function(numdates[-1]) 

    if abs(grad) < #threshold 0 gradient value
        grad = 0

    second_differential_function = gradient_function.deriv()
    second_differential = second_differential_function(numdates[-1])

    if abs(second_differential) < #threshold 0 second differential value
        second_differential = 0
    
    return (grad, second_differential)


#function returning a tuple of (X, Y, Z) for each station 
def X_Y_Z(station):

    X = (station.typical_range[1]) * 0. #determine value for X
    Y = (station.typical_range[1]) * 1. #determine value for Y 
    Z = (station.typical_range[1]) * 1. #determine value for Z

    return (X, Y, Z)

#function sorting a station to an appropriate list 
def append_station_to_list(recent_level, grad, second_differential, X, Y, Z, rel_high, station, severe_list, high_list, medium_list, low_list):
    if recent_level >= Z:
        if grad > 0 or grad == 0:
            severe_list.append(station)

        elif grad < 0 and second_differential < 0:
            severe_list.append(station)

        else:
            high_list.append(station)
            
    if recent_level >= Y and recent_level < Z:
        if grad > 0:
            severe_list.append(station)
            
        elif grad == 0 and second_differential > 0:
            severe_list.append(station)
            
        elif grad == 0 and second_differential == 0:
            severe_list.append(station)
            
        elif grad == 0 and second_differential < 0:
            high_list.append(station)
            
        elif grad < 0 and second_differential > 0:
            medium_list.append(station)
            
        elif grad < 0 and second_differential == 0:
            medium_list.append(station)
            
        elif grad < 0 and second_differential > 0:
            high_list.append(station)
        
    if recent_level >= rel_high and recent_level < Y:
        if grad < 0:
            medium_list.append(station)
            
        elif grad > 0 and second_differential > 0:
            high_list.append(station)
            
        elif grad > 0 and second_differential == 0:
            high_list.append(station)

        elif grad > 0 and second_differential < 0:
            medium_list.append(station)
            
        elif grad == 0 and second_differential > 0:
            high_list.append(station)
            
        elif grad == 0 and second_differential == 0:
            high_list.append(station)

        elif grad == 0 and second_differential < 0:
            medium_list.append(station)
        
    if recent_level >= X and recent_level < rel_high:
        if grad < 0:
            low_list.append(station)
            
        elif grad > 0 and second_differential > 0:
            medium_list.append(station)

        elif grad > 0 and second_differential == 0:
            medium_list.append(station)

        elif grad > 0 and second_differential < 0:
            low_list.append(station)
            
        elif grad == 0 and second_differential > 0:
              medium_list.append(station)
            
        elif grad == 0 and second_differential == 0:
             medium_list.append(station)
            
        elif grad == 0 and second_differential < 0:
            low_list.append(station)
        
    else:
        low_list.append(station)

#function creating the list of stations for S, H, M, L 
def danger_lists():

    stations = build_station_list()
    update_water_levels(stations)
    
    severe_list = []
    high_list = []
    medium_list = []
    low_list = []

    for station in stations:

        if typical_range_consistent(station) is True:
        
            dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))

            recent_level = levels[-1]
   
            grad = gradient_and_second_deriv(levels, dates, N)[0]
            second_differential = gradient_and_second_deriv(levels, dates, N)[1]

            rel_high = station.typical_range[1]
            X = X_Y_Z(station)[0]
            Y = X_Y_Z(station)[1]
            Z = X_Y_Z(station)[2]

            append_station_to_list(recent_level, grad, second_differential, X, Y, Z, rel_high, station, severe_list, high_list, medium_list, low_list)
    
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

    for station in seperate_lists_of_stations_list[0]:
        severe_towns.append(station.town)

    for station in seperate_lists_of_stations_list[1]:
        high_towns.append(station.town)

    for station in seperate_lists_of_stations_list[2]:
        medium_towns.append(station.town)

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

    print('Towns at severe risk are:')
    for i in seperate_lists_of_towns_list[0]:
        print(f'{i}')
    
    print('Towns at high risk are:')
    for i in seperate_lists_of_towns_list[1]:
        print(f'{i}')

    print('Towns at medium risk are:')
    for i in seperate_lists_of_towns_list[2]:
        print(f'{i}')

    print('Towns at low risk are:')
    for i in seperate_lists_of_towns_list[3]:
        print(f'{i}')