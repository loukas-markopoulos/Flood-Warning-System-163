from floodsystem.finalprogramme import gradient_and_second_deriv, X_Y_Z, append_station_to_list, danger_lists, list_of_towns, final_print
from floodsystem.stationdata import MonitoringStation
from unittest.mock import patch, call
from floodsystem.flood import stations_over_level_threshold

Test1 = MonitoringStation("Test1 station", "Test1 measure id", "1", (70, 0), (0, 100), "Test1 river", "Test1 town")
Test1.latest_level = 10
Test2 = MonitoringStation("Test2 station", "Test2 measure id", "2", (80, 100), (10, 1000), "Test2 river", "Test2 town")
Test2.latest_level = 10
Test3 = MonitoringStation("Test3 station", "Test3 measure id", "3", (0, 180), None, "Test3 river", "Test3 town")
Test3.latest_level = 10

#following tests just for danger_lists testing
Test4 = MonitoringStation("Test4 station", "Test4 measure id", "4", (20, 30), (20, 60), "Test4 river", "Test4 town")
Test4.latest_level = 10
Test5 = MonitoringStation("Test5 station", "Test5 measure id", "5", (0, 0), (80, 170), "Test5 river", "Test5 town")
Test5.latest_level = 10
Test6 = MonitoringStation("Test6 station", "Test6 measure id", "6", (0, 100), (0, 290), "Test6 river", "Test6 town")
Test6.latest_level = 10
Testlist = [Test1, Test2, Test3, Test4, Test5, Test6]



def test_X_Y_Z():
    threshold_values = X_Y_Z(Test1)
    assert threshold_values[0] == Test1.typical_range[1] * 0.8
    assert threshold_values[1] == Test1.typical_range[1] * 2.0
    assert threshold_values[2] == Test1.typical_range[1] * 3.0
    threshold_values3 = X_Y_Z(Test3)
    assert threshold_values3 == [None, None, None]


test_X_Y_Z()


severe_list, high_list, medium_list, low_list = [], [], [], []

def test_append_station_to_list():
    append_station_to_list(250, -10, 30, 80, 200, 300, Test1.typical_range[1], Test1.name, severe_list, high_list, medium_list, low_list)
    append_station_to_list(1500, 0, 20, 800, 2000, 3000, Test2.typical_range[1], Test2.name, severe_list, high_list, medium_list, low_list)
    assert medium_list == [Test1.name]
    assert high_list == [Test2.name]


test_append_station_to_list()



severe_list = [Test1]
high_list = [Test2]
medium_list = [Test3]
low_list = []
separate_lists_of_stations_list = [severe_list, high_list, medium_list, low_list]

def test_list_of_towns():
    separate_lists_of_towns_list = list_of_towns(separate_lists_of_stations_list)
    assert separate_lists_of_towns_list == [["Test1 town"], ["Test2 town"], ["Test3 town"], []]


test_list_of_towns()


separate_lists_of_towns_list = [["Test1 town"], ["Test2 town"], ["Test3 town"], []]
@patch("builtins.print")

def test_final_print(mock_print):
    final_print(separate_lists_of_towns_list)
    mock_print.assert_has_calls(mock_print.mock_calls, [call("Towns at severe risk are:"), call("Test1 town"), call("Towns at high risk are:"), call("Test2 town"), call("Towns at medium risk are:"), call("Test3 town"), call("No towns are at low risk.")])


test_final_print()