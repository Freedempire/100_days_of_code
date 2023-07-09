import requests

# URL = 'http://api.open-notify.org/iss-now.json'

# response = requests.get(URL)

# # raise exception if unsuccessful status code returned
# response.raise_for_status()
# print(response)
# data = response.json()
# print(data)

URL = 'https://api.sunrise-sunset.org/json'
my_lat = -33.846017
my_lng = 151.038025
params = {
    'lat': my_lat,
    'lng': my_lng,
}
response = requests.get(URL, params=params)
response.raise_for_status()
data = response.json()
print(data)