import requests

# def get_data(station, city, state, country, key):
#     url = 'api.airvisual.com/v2/station?station={}&city={}&state={}&country={}&key={}'.format(
#         station, city, state, country, key)
#     payload = {}
#     headers = {}
#     response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False, timeout=None)
#     print(response.text)
#
key = '3ZNrZ3EdKhNrQP54Q'
# station = '59 st'
# city = 'New York'
# state = 'New York'
# country = 'USA'


# # STATES IN USA
# import requests
# url = 'http://api.airvisual.com/v2/states?country=USA&key={}'.format(key)
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
# print(response.text)


# # CITIES IN NEW YORK STATE
# import requests
# url = 'http://api.airvisual.com/v2/cities?state=New York&country=USA&key={}'.format(key)
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
# print(response.text)



# # STATIONS IN NEW YORK CITY
# import requests
# url = 'http://api.airvisual.com/v2/stations?city=New York&state=New York&country=USA&key={}'.format(key)
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=None)
# print(response.text)


# # SPECIFIED STATION DATA
# import requests
# url = 'http://api.airvisual.com/v2/station?station=US Embassy in Beijing&city=Beijing&state=Beijing&country=China&key={}'.format(key)
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=None)
# print(response.text)