from floodsystem.geo import stations_by_distance, stations_by_river, stations_within_radius, rivers_by_station_number, rivers_with_station
from floodsystem.station import MonitoringStation

Test1 = MonitoringStation("Test1 station", "Test1 measure id", "1", (70, 0), (-100, -10), "Test1 river", "Test1 town")
Test2 = MonitoringStation("Test2 station", "Test2 measure id", "2", (80, 100), (-10, 1000), "Test2 river", "Test2 town")
Test3 = MonitoringStation("Test3 station", "Test3 measure id", "3", (0, 180), None, "Test3 river", "Test3 town")

Testlist = [Test1, Test2, Test3]

def test_stations_by_distance():
    closestations = stations_by_distance(Testlist, (0,0))
    assert closestations[0][1] == Testlist[0].town
    assert closestations[1][1] == Testlist[1].town
    assert closestations[2][1] == Testlist[2].town

def test_stations_within_radius():
    radiusstations = stations_within_radius(Testlist, (0,0), 10000)
    assert radiusstations[0] == Testlist[0].name

def test_rivers_with_station():
    stationrivers = rivers_with_station(Testlist)
    assert stationrivers == ["Test1 river", "Test2 river", "Test3 river"]

def test_stations_by_river():
    riverstations = stations_by_river(Testlist)
    assert riverstations[Testlist[0].river] == [Testlist[0].name]
    assert riverstations[Testlist[1].river] == [Testlist[1].name]
    assert riverstations[Testlist[2].river] == [Testlist[2].name]

def test_rivers_by_station_number():
    riversgreateststations = rivers_by_station_number(Testlist, 1)
    assert riversgreateststations[0] == ("Test1 river", 1)
    assert riversgreateststations[1] == ("Test2 river", 1)
    assert riversgreateststations[2] == ("Test3 river", 1)


test_stations_by_distance()
test_stations_within_radius()
test_rivers_with_station()
test_stations_by_river()
test_rivers_by_station_number()