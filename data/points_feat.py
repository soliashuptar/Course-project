import json
import sys
sys.path.append("..")
from map.radius import Circle

with open('../data/newdata.json', 'r') as f:
    JSON_DATA = json.load(f)

# print(JSON_DATA['info'])

DATA = JSON_DATA['info']

points = []
# 2019/08.05
for info in DATA:
    # print('-'.join(info['date'].split('/')[::-1]))

    dct = {
        'station': info['station'],
        'time': '-'.join(info['date'].split('/')[::-1]) + "T" + info['time'],
        'popup': 'Station: {}'.format(info['station']),
        'coordinates': [info['coords'][1], info['coords'][0]],
        'entrances': info['entrances'],
        'exits': info['exits']
    }

    points.append(dct)


# print(points)
# points = list(set(points))
# print(points)


features = []
# features = [{
#             'type': 'Feature',
#             'geometry': {
#                 'type': 'Point',
#                 'coordinates': point['coordinates'],
#             },
#             'properties': {
#                 'times': point['time'].replace('/', '-'),
#                 'popup': "Station: {}<br> Entrances: {}".format(point['station'], abs(point['entrances'] - point['exits'])),
#                 'icon': 'circle',
#                 'iconstyle': {
#                     'fillColor': 'red' if Circle(point['coordinates'], point['entrances'], point['exits']).count_radius() else '#07eb96',
#                     'fillOpacity': 0.3,
#                     'stroke': 'false',
#                     'radius': Circle(point['coordinates'], point['entrances'], point['exits']).count_radius()
#                     }
#             }
#         }
#         for point in points
#
# ]
#
for point in points:
    stat = point['station']
    # print(point['time'])
    time = point['time']
    print(time)
    coords = point['coordinates']
    entr = point['entrances']
    exits = point['exits']
    circle = Circle(coords, entr, exits)
    radius = circle.count_radius()
    popup = "Station: {}<br> Entrances: {}".format(stat, abs(entr - exits))
    color = 'red'
    if radius > 50:
        color = '#07eb96'  # green
    elif radius < 30:
        color = '#0abde3'  # blue
    elif radius <= 50:
        color = '#f04822'  # orange
    dct = {
            'type': 'Feature',
            'geometry': {
                'type': 'MultiPoint',
                'coordinates': [coords],
            },
            'properties': {
                'times': [time],
                'popup': popup,
                'icon': 'circle',
                'iconstyle': {
                    'fillColor': color,
                    'fillOpacity': 0.3,
                    'stroke': 'false',
                    'radius': radius
                    }
            }
        }

    features.append(dct)

# print(features)
features.append(
    {
        'type': 'Feature',
        'geometry': {
            'type': 'LineString',
            'coordinates': [
                info['coords'] for info in DATA
            ],
        },
        'properties': {
            'popup': 'Current address',
            'times': sorted(list(set(['-'.join(info['date'].split('/')[::-1]) + "T" + info['time']]))),
            'icon': 'circle',
            'iconstyle': {
                'fillColor': 'green',
                'fillOpacity': 0.6,
                'stroke': 'false',
                'radius': 13
            },
            'style': {'weight': 0},
            'id': 'man'
        }
    }
)
print(features)
# print(sorted(list(set([info['date'] for info in DATA]))))
# print(list(set([info['date'] for info in DATA])))