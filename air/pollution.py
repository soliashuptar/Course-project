import requests

# # STATIONS IN NEW YORK CITY
key = 'a8c65185c0ea457f8be6fb6f51e2c8cd'
url = 'https://api.breezometer.com/air-quality/v2/current-conditions?lat=40.734464&lon=-73.994858&key={}'.format(key) #at the moment

url_1 = "https://api.breezometer.com/air-quality/v2/historical/hourly?lat=48.857456&lon=2.354611&key=YOUR_API_KEY&datetime=2019-05-14T14:00:00"

url_2 = "https://api.breezometer.com/air-quality/v2/historical/hourly?lat=40.734464&lon=-73.994858&key={}&start_datetime=2019-05-14T14:00:00&end_datetime=2019-05-14T16:00:00".format(key)
payload = {}
headers = {}
response = requests.request('GET', url_2, headers=headers, data=payload, allow_redirects=False, timeout=None)
print(response.text)