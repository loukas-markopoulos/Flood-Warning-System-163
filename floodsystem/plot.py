import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num

# colab notebook 8
# 2E
def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels)

    if dates != None and levels != None:

        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=90);
        plt.title(f'{station.name}')

        plt.tight_layout()

        plt.axhline(y = f'{station.typical_range[0]}', color = 'r')
        plt.axhline(y = f'{station.typical_range[1]}', color = 'r')

        plt.show()

    else:

        print("No plot available for", station.name, "due to lack of dates data")

    return

# polynomial best fit plot
# 2F
def plot_water_level_with_fit(station, dates, levels, p):
    
    poly, d0 = polyfit(dates, levels, p)
    x = date2num(dates)

    if poly != None and d0 != None:

        plt.plot(x-d0, poly(x-d0))
        plt.title(f'{station.name, "best fit"}')
        plt.xlabel('date')
        plt.ylabel('water level (m)')

        plt.tight_layout()

        plt.axhline(y = f'{station.typical_range[0]}', color = 'r')
        plt.axhline(y = f'{station.typical_range[1]}', color = 'r')

        plt.show()

    else:

        print("No best fit plot available for", station.name, "due to lack of dates data")

    return

