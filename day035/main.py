import os

import requests
import dotenv

# https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html
# https://ss64.com/nt/setx.html
# can store api key in system environment variables, for example, setx api_key 189a963fa9d7b5d7dabd13ed8afb72b3
# then use os.environ.get('api_key') to retrieve it
# use dotenv library to load environment variables from .env file

dotenv.load_dotenv()
API_KEY = os.environ.get('API_KEY')
API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
PARAMS = {
    'lat': -35.882,
    'lon': 148.502,
    # 'lat': -33.85970379353684,
    # 'lon': 151.02173110089555,
    'appid': API_KEY,
    'units': 'metric',
}

response = requests.get(API_ENDPOINT, PARAMS)
response.raise_for_status()
results = response.json()['list']

for period in results[:4]:
    # https://openweathermap.org/weather-conditions
    if period['weather'][0]['id'] < 700:
        print(period['weather'][0]['main'])
        break