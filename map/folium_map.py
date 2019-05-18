import folium
from folium import plugins
import sys

sys.path.append("..")

from data import points_feat
from data import pollution

main_path = '../data/newdata.json'
flask_path = '../CourseProject/data/newdata.json'


def create_map():
    """
    Function creates a map and saves it to templates folder
    :return:
    """

    points = points_feat.create_points(flask_path)
    FEATURES = points['features']
    points_COORDINATES = points['coordinates']
    DEF_TIME = points['set-time']

    folium_map = folium.Map(location=[40.738, -73.98],
                            zoom_start=12,
                            tiles="CartoDB dark_matter")

    # MiniMap plugin
    minimap = plugins.MiniMap()
    folium_map.add_child(minimap)

    # Fullscreen plugin
    plugins.Fullscreen(
        position='topright',
        title='Expand me',
        title_cancel='Exit me',
        force_separate_button=True
    ).add_to(folium_map)

    # Timestamp plugin
    plugins.TimestampedGeoJson(
        {
            'type': 'FeatureCollection',
            'features': FEATURES,

        }
        , period='PT4H'
        , add_last_point=True
        , duration='PT1M'
    ).add_to(folium_map)

    coordinates = []
    for c in points_COORDINATES:
        newlst = [c[1], c[0]]
    aqi = pollution.get_air_data(newlst, DEF_TIME)[0] / 2.5
    newlst.append(aqi)
    coordinates.append(newlst)

    heat_map = plugins.HeatMap(coordinates, radius=50)
    heat_map.layer_name = 'Air Quality'
    folium_map.add_child(heat_map)

    folium_map.add_child(folium.LayerControl())

    print('> Done.')
    folium_map.save("../CourseProject/templates/my_map.html")


if __name__ == "__main__":
    create_map()
