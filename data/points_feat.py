import json
import sys

sys.path.append("..")
from map.radius import Circle


# '../data/newdata.json'
def load_data(filename):
    """Function loads data from json"""
    with open(filename, 'r') as f:
        JSON_DATA = json.load(f)
        return JSON_DATA['info']


def create_points(filename):
    """
    Function which creates points with scroller on a map
    :param filename:
    :return: dict
    """
    DATA = load_data(filename)

    points = []
    # 2019/08.05
    for info in DATA:
        dct = {
            'station': info['station'],
            'time': '-'.join(info['date'].split('/')[::-1]) + "T" + info['time'],
            'popup': 'Station: {}'.format(info['station']),
            'coordinates': [info['coords'][1], info['coords'][0]],
            'entrances': info['entrances'],
            'exits': info['exits']
        }

        points.append(dct)

    features = []
    coordinates = []

    for point in points:
        stat = point['station']
        # print(point['time'])
        time = point['time']
        print(time)
        coords = point['coordinates']

        if coords not in coordinates:
            coordinates.append(coords)

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
                    'fillOpacity': 0.15,
                    'stroke': 'false',
                    'radius': radius
                }
            }
        }

        features.append(dct)

    def_time = time
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
    result = {
        'features': features,
        'coordinates': coordinates,
        'set-time': def_time
    }
    return result
