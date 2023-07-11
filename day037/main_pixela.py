import random
import secrets
import string
import json
from datetime import datetime, timezone

import requests


def urljoin(*args):
    """Join given url parts into an complete url.
    args: strings of urls parts, arbitrary number
    The starting '/' of the first part and the ending '/' of the last part will be kept.
    """

    # return '/'.join(map(lambda part: part.strip('/'), args))
    if len(args) == 0:
        return
    if len(args) == 1:
        return args[0]
    url = ''
    for index, arg in enumerate(args):
        if index == 0:
            url += arg.rstrip('/') if arg.endswith('/') else arg
        else:
            url += arg if arg.startswith('/') else '/' + arg
    return url


def get_token():
    """Get token from file or create a new one if file not found and then store it to settings.json."""
    try:
        with open('settings.json') as f:
            token = json.load(f)['token']
    except:
        # token = random.getrandbits(128) # only contains numbers
        token = secrets.token_hex(nbytes=64)
        with open('settings.json', 'w') as f:
            json.dump(dict(token=token), f, indent=4)
    return token

def store_username():
    try:
        with open('settings.json') as f:
            settings = json.load(f)
            settings['username'] = USERNAME
        with open('settings.json', 'w') as f:
            json.dump(settings, f, indent=4)
    except FileNotFoundError as e:
        print(e)
        print('Please generate the token first.')


def generate_id(length=16):
    id = random.choice(string.ascii_lowercase)
    for _ in range(length - 1):
        id += random.choice(string.ascii_lowercase + string.digits)
    return id


def get_today():
    return datetime.now().astimezone(timezone.utc).strftime('%Y%m%d')

def create_user():
    params = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }

    response = requests.post(urljoin(BASE_URL, CREATE_USER), json=params)
    response.raise_for_status()
    print(response.json())


def create_graph(name, unit, type='int', color='shibafu', id=None):
    """
    Create a new graph and store its info into to settings.json.
    unit: Unit of the quantity recorded in the pixelation graph, e.g. commit, kilogram, calory.
    type: Type of quantity to be handled in the graph. Only int or float are supported.
    color: shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black).
    id: ID for identifying the pixelation graph. Validation rule: ^[a-z][a-z0-9-]{1,16}.
    """
    if id is None:
        id = generate_id()
    headers = {
        'X-USER-TOKEN': TOKEN
    }
    body = {
        'id': id,
        'name': name,
        'unit': unit,
        'type': type,
        'color': color
    }
    response = requests.post(urljoin(BASE_URL, CREATE_USER, USERNAME, CREATE_GRAPH), json=body, headers=headers)
    response.raise_for_status()
    print(response.json())
    if response.json()['isSuccess']:
        with open('settings.json') as f:
            settings = json.load(f)
        graphs = settings.get('graphs')
        if graphs is None:
            settings.update({'graphs': []})
            graphs = settings['graphs']
        graphs.append(dict(id=id, name=name, unit=unit, type=type, color=color))
        with open('settings.json', 'w') as f:
            json.dump(settings, f, indent=4)


def get_graph(name=None):
    try:
        with open('settings.json') as f:
            graphs = json.load(f)['graphs']
    except Exception as e:
        print(e)
    else:
        result_count = 0
        for graph in graphs:
            if name is None or name == graph['name']:
                print(urljoin(BASE_URL, CREATE_USER, USERNAME, CREATE_GRAPH, graph['id']) + '.html')
                result_count += 1
        if result_count == 0:
            print(f'There is no graph named "{name}".')


def post_pixel(name, quantity, id=None, date=get_today()):
    """
    Update the named graph. If multiple graphs share the same name, only one get updated when id is None.
    If id is not None, only the graph with same id will be updated.
    name: str
    quantity: str
    id: str, default to None.
    date: str, the date on which the quantity is to be recorded. It is specified in yyyyMMdd format.
    """
    headers = {
        'X-USER-TOKEN': TOKEN
    }
    body = {
        'quantity': quantity,
        'date': date
    }
    try:
        with open('settings.json') as f:
            graphs = json.load(f)['graphs']
    except Exception as e:
        print(e)
        print('settings.json does not exist or no graphs yet.')
    else:
        graph_found = False
        for graph in graphs:
            if id is None and graph['name'] == name or graph['id'] == id:
                graph_found = True
                response = requests.post(urljoin(BASE_URL, CREATE_USER, USERNAME, CREATE_GRAPH, graph['id']), json=body, headers=headers)
                print(response.json())
                if not response.json()['isSuccess']:
                    while response.json().get('isRejected'):
                        response = requests.post(urljoin(BASE_URL, CREATE_USER, USERNAME, CREATE_GRAPH, graph['id']), json=body, headers=headers)
                        print(response.json())
                print(f'Pixel of graph \"{graph["name"]}\" posted for date {date}.')
                break
        if not graph_found:
            print(f'There is no graph named "{name}".')
        

def delete_graph(id):
    headers = {
        'X-USER-TOKEN': TOKEN
    }
    try:
        with open('settings.json') as f:
            settings = json.load(f)
            graphs = settings['graphs']
    except Exception as e:
        print(e)    
        print('settings.json does not exit or no graphs yet.')
    else:
        graph_found_index = None
        for index, graph in enumerate(graphs):
            if graph['id'] == id:
                graph_found_index = index
                break
        if graph_found_index is not None:
            response = requests.delete(urljoin(BASE_URL, CREATE_USER, USERNAME, CREATE_GRAPH, id), headers=headers)
            print(response.json())
            if response.json()['isSuccess']:
                graphs.pop(graph_found_index)
                with open('settings.json', 'w') as f:
                    json.dump(settings, f, indent=4)
        else:
            print(f'There is no graph with the id: "{id}"')


BASE_URL = 'https://pixe.la'
CREATE_USER = '/v1/users'
CREATE_GRAPH = '/graphs'
USERNAME = 'freedempire'
TOKEN = get_token()
PERSON_URL = 'https://pixe.la/@freedempire'

# store_username()
# create_user()

# create_graph('English words', 'words')
# create_graph('Reading pages', 'pages')
# create_graph('Programming hours', 'hours')

# get_graph()
# get_graph('Programming')
# get_graph('Reading pages')
# get_graph('English words')

# today = get_today()
# print(today)
# print(type(today))

# post_pixel('Reading pages', '10')
# post_pixel('English words', '10')
# post_pixel('Programming hours', '10', date='20230708')
# post_pixel('Programming hours', '3', date='20230707')
# post_pixel('Programming hours', '3', date='20230706')
# post_pixel('Programming hours', '2', date='20230705')
# post_pixel('Programming hours', '4', date='20230704')
# post_pixel('Programming hours', '5', date='20230703')
# post_pixel('Programming hours', '10', date='20230702')
# post_pixel('Programming hours', '13', date='20230701')
# post_pixel('Programming hours', '3', date='20230601')
# post_pixel('Programming hours', '4', date='20230602')
# post_pixel('Programming hours', '10', date='20230603')
# post_pixel('Programming hours', '11', date='20230604')
# post_pixel('Programming hours', '3', date='20230605')
# post_pixel('Programming hours', '4', date='20230606')
# post_pixel('Programming hours', '2', date='20230607')
# post_pixel('Programming hours', '2', date='20230608')
# post_pixel('Programming hours', '3', date='20230609')
# post_pixel('Programming hours', '8', date='20230610')
# post_pixel('Programming hours', '9', date='20230611')
# post_pixel('Programming hours', '3', date='20230612')
# post_pixel('Programming hours', '4', date='20230613')
# post_pixel('Programming hours', '2', date='20230614')
# post_pixel('Programming hours', '3', date='20230615')
# post_pixel('Programming hours', '4', date='20230616')
# post_pixel('Programming hours', '13', date='20230617')
# post_pixel('Programming hours', '9', date='20230618')
# post_pixel('Programming hours', '1', date='20230619')
# post_pixel('Programming hours', '3', date='20230620')
# post_pixel('Programming hours', '4', date='20230621')
# post_pixel('Programming hours', '5', date='20230622')
# post_pixel('Programming hours', '2', date='20230623')
# post_pixel('Programming hours', '12', date='20230624')
# post_pixel('Programming hours', '12', date='20230625')
# post_pixel('Programming hours', '3', date='20230626')
# post_pixel('Programming hours', '3', date='20230627')
# post_pixel('Programming hours', '3', date='20230628')
# post_pixel('Programming hours', '4', date='20230629')
# post_pixel('Programming hours', '3', date='20230630')

# create_graph('Programming hourss', 'hourss')
# delete_graph('rrgrwbsyitb2grdx')

post_pixel('Programming hours', '4')
post_pixel('English words', '10')
post_pixel('Reading pages', '15')