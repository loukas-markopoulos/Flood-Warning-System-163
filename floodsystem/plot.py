import matplotlib.pyplot as plt
import numpy as np
import math as math
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num

# colab notebook 8
# 2E
def plot_water_levels(station, dates, levels):

    if len(dates) != len(levels):
        raise IndexError

    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=90);
    plt.title(f'{station.name}')

    plt.tight_layout()

    low_level_list = [station.typical_range[0]]*len(dates)
    high_level_list = [station.typical_range[1]]*len(dates)

    plt.plot(dates, low_level_list, color = 'r')
    plt.plot(dates, high_level_list, color = 'r')

    plt.show()

    return

# polynomial best fit plot
# 2F
def plot_water_level_with_fit(station, dates, levels, p):

    if len(dates) != len(levels):
        raise IndexError
    
    poly, d0 = polyfit(dates, levels, p)
    x = date2num(dates)
    indicies = []
    for i in range(len(x)):
        if math.isnan(x[i]) == True:
            indicies.append(i)
    
    x = np.delete(x, indicies)

    if poly != None and d0 != None:

        plt.plot(x-d0, poly(x-d0))
        plt.title(f'{station.name, "best fit"}')
        plt.xlabel('date')
        plt.ylabel('water level (m)')

        plt.tight_layout()

        low_level_list = [station.typical_range[0]]*len(x)
        high_level_list = [station.typical_range[1]]*len(x)

        plt.plot(x-d0, low_level_list, color = 'r')
        plt.plot(x-d0, high_level_list, color = 'r')

        plt.show()

    else:

        print("No best fit plot available for", station.name, "due to lack of dates data")

    return

