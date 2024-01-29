import numpy as np
import matplotlib as plt

def polyfit(dates, levels, p):

    x = plt.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)
    plt.plot(x, y, '.')
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1-x[0]))
    plt.show()

    return poly, d0