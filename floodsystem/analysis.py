import numpy as np
from matplotlib.dates import date2num

def polyfit(dates, levels, p):

    x = date2num(dates)
    poly = None
    d0 = None

    if len(x) == 0:
        return poly, d0
    
    y = levels
    d0 = x[-1]
    p_coeff = np.polyfit(x - d0, y, p)
    poly = np.poly1d(p_coeff)

    return poly, d0




