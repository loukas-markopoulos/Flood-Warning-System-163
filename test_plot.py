import unittest
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.station import MonitoringStation

Test1 = MonitoringStation("Test1 station", "Test1 measure id", "1", (70, 0), (-100, -10), "Test1 river", "Test1 town")
Testlist = [Test1]

#check if plot appears with no errors
class PlotMethods(unittest.TestCase):

    def test_plot_water_levels(self):
        self.assertRaises(IndexError, plot_water_levels, Testlist[0], [2024-2-12, 2024-2-11, 2024-2-10], [4, 1])
        self.assertRaises(IndexError, plot_water_levels, Testlist[0], [2024-2-12, None], [4, 1, 0])
        self.assertRaises(IndexError, plot_water_levels, Testlist[0], [2024-2-12, 2024-2-11, 2024-2-10],[4, None])

    def test_plot_water_level_with_fit(self):
        self.assertRaises(IndexError, plot_water_level_with_fit, Testlist[0], (2024-2-12, 2024-2-11, 2024-2-10, 2024-2-9), (4, 0, -1), 2)
        self.assertRaises(IndexError, plot_water_level_with_fit, Testlist[0], (2024-2-12, 2024-2-9), (4, 1, -1), 2)
        self.assertRaises(IndexError, plot_water_level_with_fit, Testlist[0], (2024-2-12, 2024-2-11, None, 2024-2-9), (4, 0, -1), 2)

if __name__ == '__main__':
    unittest.main()