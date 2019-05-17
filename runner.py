from data import info, json_data
from map import folium_map


def main(day):
    '''
    Main function including all other sub-main functions
    :return: None
    '''
    # loading data
    info.get_info_with_last(day)
    # converting data to json
    amount = 800
    json_data.to_json('../CourseProject/data/data.txt', '../CourseProject/data/newdata.json', amount)
    # creating a map
    folium_map.create_map()
    return True


if __name__ == "__main__":
    main('MON')
