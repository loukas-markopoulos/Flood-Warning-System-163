import matplotlib.pyplot as plt
from datetime import datetime, timedelta
#colab notebook 8
def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=90);
    plt.title(f'{station.name}')

    plt.tight_layout()

    plt.axhline(y = f'{station.typical_range[1]}')
    plt.axhline(y = f'{station.typical_range[0]}')

    plt.show()

    return