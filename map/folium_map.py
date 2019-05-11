import folium
import json

from folium import plugins
from folium.plugins import TimestampedGeoJson

from radius import Circle

folium_map = folium.Map(location=[40.738, -73.98],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")
fg_hc = folium.FeatureGroup(name="Stations")
with open("../data/newdata.json") as file:
    data = json.load(file)
    for line in data['info']:
        coords = line['coords']
        entr = line['entrances']
        exits = line['exits']
        circle = Circle(coords, entr, exits)
        radius = circle.count_radius()
        if radius > 50:
            color = 'green'
        elif radius < 30:
            color = 'blue'
        elif radius < 50:
            color = 'orange'
        fg_hc.add_child(folium.CircleMarker(location=line['coords'], radius=radius, popup=line['station'], color=color, fill=True))

folium_map.add_child(fg_hc)

minimap = plugins.MiniMap()
folium_map.add_child(minimap)

plugins.Fullscreen(
    position='topright',
    title='Expand me',
    title_cancel='Exit me',
    force_separate_button=True
).add_to(folium_map)

folium_map.add_child(folium.LayerControl())


# TimestampedGeoJson(
#         {
#             'type': 'FeatureCollection',
#             'features': features
#         }
#         , period='P1M'
#         , add_last_point=True
#         , auto_play=False
#         , loop=False
#         , max_speed=1
#         , loop_button=True
#         , date_options='YYYY/MM//DD'
#         , time_slider_drag_update=True,
#         duration='P2M'
#     ).add_to(folium_map)



print('> Done.')
folium_map.save("../templates/my_map.html")