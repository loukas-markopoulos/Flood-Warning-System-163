from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.station import MonitoringStation

Test1 = MonitoringStation("Test1 station", "Test1 measure id", "1", (70, 0), (-100, -10), "Test1 river", "Test1 town")
Testlist = [Test1]

#check if plot appears with no errors
def test_plot_water_levels():
    plot_water_levels(Testlist[0], (2024-2-12, 2024-2-11, 2024-2-10), (4, 1, 0))
    plot_water_levels(Testlist[0], (2024-2-12, 2024-2-11, None), (4, 1, 0))
    plot_water_levels(Testlist[0], (2024-2-12, 2024-2-11, 2024-2-10), (4, 1, None))

def test_plot_water_level_with_fit():
    plot_water_level_with_fit(Testlist[0], (2024-2-12, 2024-2-11, 2024-2-10, 2024-2-9), (4, 1, 0, -1), 2)
    plot_water_level_with_fit(Testlist[0], (2024-2-12, 2024-2-11, 2024-2-9), (4, 1, -1), 2)
    plot_water_level_with_fit(Testlist[0], (2024-2-12, 2024-2-11, None, 2024-2-9), (4, 1, 0, -1), 2)


test_plot_water_levels()
test_plot_water_level_with_fit()