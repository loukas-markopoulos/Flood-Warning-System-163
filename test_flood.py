from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_over_level_threshold, stations_highest_rel_level

#no coordinates being tested for flood so coordinates are set to (0,0)
Test1 = MonitoringStation("Test1 station", "Test1 measure id", "1", (0, 0), (-100, -10), "Test1 river", "Test1 town")
Test2 = MonitoringStation("Test2 station", "Test2 measure id", "2", (0, 0), (0, -10), "Test2 river", "Test2 town")
Test3 = MonitoringStation("Test3 station", "Test3 measure id", "3", (0, 0), None, "Test3 river", "Test3 town")
Test4 = MonitoringStation("Test4 station", "Test4 measure id", "4", (0, 0), (1, 5), "Test4 river", "Test4 town")


Testlist = [Test1, Test2, Test3]
tol = 1.4
Test1.latest_level = 80
# ratio = (80 - (-100)) / (-10 - (-100)) = 2
Test2.latest_level = 100
# self.typical_range[0] > self.typical_range[1] so ratio = None
Test3.latest_level = 100000
# self.typical_range = None so ratio = None
Test4.latest_level = 1.5
# ratio = (1.5 - 1) / (5 - 1) = 0.125


def test_stations_over_level_threshold():
    list_over_threshold = stations_over_level_threshold(Testlist, tol)
    assert list_over_threshold == [(Test1.name, 2.0)]

def test_stations_highest_relative_level():
    highest_relative_level = stations_highest_rel_level(Testlist, 1)
    assert highest_relative_level == [(Test1.name, 2.0)]

test_stations_over_level_threshold()
test_stations_highest_relative_level()