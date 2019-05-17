import random
import requests

key = 'a8c65185c0ea457f8be6fb6f51e2c8cd'


def get_air_data(coords, date):
    """
    Function loads data from API about air quality
    :param coords: list
    :param date: string
    :return: list/tuple
    """
    print("Getting air quality data...")
    lat = coords[0]
    lon = coords[1]
    new_date = date.replace('/', '-')
    sp = new_date.split('-')
    day = sp[1]
    month = sp[0]
    year = sp[2]
    new_date = year + '-' + month + '-' + day
    # print(new_date)
    URL = 'https://api.breezometer.com/air-quality/v2/historical/hourly?lat={}&lon={}&key={}&datetime={}T18:00:00'.format(
        lat, lon, key, new_date
    )
    payload = {}
    headers = {}
    response = requests.request('GET', URL, headers=headers, data=payload, allow_redirects=False, timeout=None)
    # print(response.json())
    DATA = response.json()
    try:
        info = DATA['data']['indexes']['baqi']
        aqi = info['aqi']
        color = info['color']
        category = info['category']
        return (aqi, color, category)
    except:
        print('error.', DATA)
        return [random.randint(40, 60)]


if __name__ == "__main__":
    coords = [40.641362, -74.017881]
    date = '05/04/2019'
    print(get_air_data(coords, date))
