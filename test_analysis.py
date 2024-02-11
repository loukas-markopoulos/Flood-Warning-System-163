from floodsystem.analysis import polyfit
from datetime import datetime
from matplotlib.dates import date2num

def test_polyfit():
    poly, d0 = polyfit((2024-2-12, 2024-2-11, 2024-2-10), (4, 1, 0), 3)
    assert d0 == (date2num(2024-2-10))

test_polyfit()
