import numpy as np
from matplotlib.dates import date2num
import math as math

# 2F
#plot of dates and levels
def polyfit(dates, levels, p):

    x = date2num(dates)
    y = levels
    poly = None
    d0 = None
    indicies = []

    if len(x) == 0:
        return poly, d0
    
    for i in range(len(x)):
        if math.isnan(x[i]) == True or y[i] == None:
            indicies.append(i)

    x = np.delete(x, indicies)
    y = np.delete(y, indicies)
    
    d0 = x[-1]
    p_coeff = np.polyfit(x - d0, y, p)
    poly = np.poly1d(p_coeff)

    return poly, d0




