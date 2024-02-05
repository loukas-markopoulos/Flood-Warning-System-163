from floodsystem.analysis import polyfit()
from matplotlib.dates import date2num

#function returning the gradient - include approximation for 0
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

#function creating the list of stations for S, H, M, L 
def danger_lists(station, levels, dates, p):
   
    severe_list = []
    high_list = []
    medium_list = []
    low_list = []
   
    recent_level = levels[-1]
   
    grad = gradient_and_second_deriv(levels, dates, p)[0]
    second_differential = gradient_and_second_deriv(levels, dates, p)[1]

    rel_high = station.typical_range[1]
    X = X_Y_Z(station)[0]
    Y = X_Y_Z(station)[1]
    Z = X_Y_Z(station)[2]

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
    
    completed




        

    
        
        
      


#function creating the list of stations for H


#function creating the list of stations for M


#function creating the list of stations for L



#function converting the list of stations to list of towns that are within radius R of the station

#function printing the seperate lists