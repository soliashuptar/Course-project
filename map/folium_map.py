import folium
import json

from folium import plugins

from radius import Circle

import sys
sys.path.append("..")

from data.points_feat import features, points
# import data.json_data
from data import json_data

folium_map = folium.Map(location=[40.738, -73.98],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")
fg_hc = folium.FeatureGroup(name="Stations")
with open("../data/newdata.json") as file:
    data = json.load(file)
    for line in data['info']:
        print("j")
        # print(line['coords'], line['station'])
        stat = line['station']
        coords = line['coords']
        entr = line['entrances']
        exits = line['exits']
        circle = Circle(coords, entr, exits)
        radius = circle.count_radius()
        if radius > 50:
            color = '#07eb96' #green
        elif radius < 30:
            color = '#0abde3' #blue
        elif radius < 50:
            color = '#f04822' #orange
        popup = "Station: {}<br> Entrances: {}".format(stat, abs(entr - exits))
        fg_hc.add_child(folium.CircleMarker(location=line['coords'], radius=radius, popup=popup, color=color, fill=True))

        # fg_hc.add_child(folium.CircleMarker(location=line['coords'], radius=525724, popup=line['station'], color='red'))
        # marker.add_to(folium_map)
        # print(line['station'], line['coords'])
# folium_map.add_child(fg_hc)

minimap = plugins.MiniMap()
folium_map.add_child(minimap)

plugins.Fullscreen(
    position='topright',
    title='Expand me',
    title_cancel='Exit me',
    force_separate_button=True
).add_to(folium_map)


plugins.TimestampedGeoJson(
        {
            'type': 'FeatureCollection',
            'features': features
        }
        , period='P1D'
        , add_last_point=True
        , auto_play=True
        , loop=True
        , max_speed=0.5
        , loop_button=True
        , date_options='YYYY/MM//DD'
        , time_slider_drag_update=True,
        duration='P{}D'.format(json_data.DURATION)
    ).add_to(folium_map)

folium_map.add_child(folium.LayerControl())

heatmap = plugins.HeatMap(data=[[40.738, -73.98], [40.641362, -74.017881]])
folium_map.add_child(heatmap)

print('> Done.')
folium_map.save("../templates/my_map.html")