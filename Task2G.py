from floodsystem.finalprogramme import  danger_lists, list_of_towns, final_print

def run():
    seperate_lists_of_stations_list = danger_lists()
    seperate_lists_of_towns_list = list_of_towns(seperate_lists_of_stations_list)
    final_print(seperate_lists_of_towns_list)

    return

run()