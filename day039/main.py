import os
import datetime
import json

from dotenv import load_dotenv
import requests

load_dotenv()

# findcheapest solution api key
# https://tequila.kiwi.com/portal/companies/freedempire/solutions/freedempireroundflights
ROUNDFLIGHTS_API_KEY = os.environ.get('ROUNDFLIGHTS_API_KEY')
KIWI_SERVERS = 'https://api.tequila.kiwi.com/'
KIWI_SERVERS_SEARCH = 'https://api.tequila.kiwi.com/v2'
LOCATIONS_QUERY_API = 'locations/query'
SEARCH_API = 'search'

# sheety personal flight club project bearer token
SHEETY_BEARER_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN')
# sheety project api endpoint
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')

DEPARTURE_CITY = 'London'


def urljoin(*args):
    """Join url parts together to form a complete one. '/' on both ends will be
    left unchanged if exist."""
    if len(args) == 0:
        return
    if len(args) == 1:
        return args[0]
    url = ''
    for index, arg in enumerate(args):
        if not arg.startswith('/') and index != 0:
            arg = '/' + arg
        if arg.endswith('/') and index < len(args) - 1:
            arg = arg.rstrip('/')
        url += arg
    return url


def get_date_after_str(days):
    """Return formatted string of date after certain days. Format: dd/mm/yyyy"""
    day = datetime.date.today() + datetime.timedelta(days=days)
    return day.strftime('%d/%m/%Y')


def get_from_sheety():
    """
    Retrieve flight deals info from sheety. If a city's IATA code is empty,
    search it on KIWI and update it to sheety.
    return: the updated sheety rows of flight deals info list.
    """
    headers = {
        'Authorization': 'Bearer ' + SHEETY_BEARER_TOKEN
    }

    response = requests.get(SHEETY_ENDPOINT, headers=headers)
    response.raise_for_status()
    sheety_rows = response.json()['prices']

    for sheety_row in sheety_rows:
        if not sheety_row['iataCode']:
            city_code = get_city_iata_code(sheety_row['city'])
            sheety_row['iataCode'] = city_code if city_code else 'NA'
            update_to_sheety(sheety_row)
    return sheety_rows


def update_to_sheety(sheety_row):
    """Update flight deals info to sheety."""
    headers = {
        'Authorization': 'Bearer ' + SHEETY_BEARER_TOKEN
    }
    body = {
        'price': {
            'city': sheety_row['city'],
            'iataCode': sheety_row['iataCode'],
            'lowestPrice': sheety_row['lowestPrice'],
        }
    }

    # params is all about the query string, and so is primarily used on GET requests.
    # The key take away here is that the data that was passed to params ended up
    # in the URL query string. Any string data passed in there will be correctly
    # escaped and encoded, then added to the URL.
    # data works differently: it’s all about the request body.
    response = requests.put(urljoin(SHEETY_ENDPOINT, str(sheety_row['id'])), json=body, headers=headers)
    response.raise_for_status()
    print(f'Updated: {response.json()}')


def get_destination_city_codes(sheety_rows):
    city_codes = []
    for sheet_row in sheety_rows:
        city_code = sheet_row['iataCode']
        if city_code not in ('NA', ''):
            city_codes.append(city_code) 
    return city_codes


def get_city_iata_code(city):
    """Retrieve a city's IATA code, return empty string if not available."""
    headers = {
        'apikey': ROUNDFLIGHTS_API_KEY
    }
    params = {
        'term': city,
        'location_types': 'city'
    }

    response = requests.get(urljoin(KIWI_SERVERS, LOCATIONS_QUERY_API), params=params, headers=headers)
    response.raise_for_status()
    try:
        city_code = response.json()['locations'][0]['code']
    except:
        city_code = ''
    return city_code


def search_flights(destination_city_codes):
    """Search for return flight deals in sheety"""
    departure_city = get_city_iata_code(DEPARTURE_CITY)

    if departure_city:
        headers = {
            'apikey': ROUNDFLIGHTS_API_KEY
        }

        params = {
            'fly_from': 'city:' + departure_city,
            'fly_to': ','.join(destination_city_codes),
            'date_from': get_date_after_str(1),
            'date_to': get_date_after_str(180),
            'nights_in_dst_from': 2,
            'nights_in_dst_to': 14,
            'ret_from_diff_city': False,
            'ret_to_diff_city': False,
            'one_for_city': 1,
            # 'curr': 'AUD'
        }

        response = requests.get(urljoin(KIWI_SERVERS_SEARCH, SEARCH_API), params=params, headers=headers)
        response.raise_for_status()
        return response.json()


# print(get_from_sheety())
# get_from_sheety()

with open('result.json', 'w') as f:
    json.dump(search_flights(get_destination_city_codes(get_from_sheety())), f, indent=4)


if __name__ == '__main__':
    print(urljoin('/aa/', '/bb/', '/cc/'))
    print(urljoin('/aa/', '/bb/', 'cc/'))
    print(urljoin('aa/', '/bb', '/cc/'))
    print(urljoin('aa', 'bb', 'cc/'))
    print(urljoin('aa/', 'bb/', 'cc/'))