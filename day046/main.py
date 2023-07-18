import re
import json
# import os

import requests
from bs4 import BeautifulSoup
import dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


def get_date_str():
    """Get a valid date from user input."""
    while True:
        date_str = input('Which date do you want to travel to? (date format: yyyy-mm-dd): ')
        if date_validate(date_str):
            return date_str
        else:
            print('Invalid date, try again.')


def date_validate(date_str):
    """Validate a date string for the format yyyy-mm-dd with leap year support.
    Years from 19xx to 21xx."""
    # https://stackoverflow.com/questions/24139038/regex-pattern-for-date-format-yyyy-mm-dd
    pattern = r"""^
    (?:(?:19|2[01])\d\d-(?:1[02]|0[13578])-(?:[0-2]\d|3[01])) # 31 day months
    |
    (?:(?:19|2[01])\d\d-(?:(?:11|0[469])-(?:[0-2]\d|30))) # 30 day months
    |
    (?:(?:19|2[01])(?:[02468][1235679]|[13579][01345789])|1900|2100)-02-(?:[01]\d|2[0-8]) # Non leap year
    |
    (?:(?:(?:19|21)(?!00)|20)(?:[02468][048]|[13579][26]))-02-(?:[01]\d|2[0-9]) # Leap year
    $"""
    regex_obj = re.compile(pattern, re.X)
    return True if regex_obj.match(date_str) else False


def urljoin(*args):
    """ Join url parts together. The starting and ending '/' will not be trimmed if exist."""
    if len(args) == 0:
        return
    if len(args) == 1:
        return args[0]
    url = ''
    for index, arg in enumerate(args):
        if index == 0:
            url += arg if arg.endswith('/') else arg + '/'
        else:
            url += arg.lstrip('/') if arg.startswith('/') else arg
    return url

# by using dotenv.load_dotenv(), all the variables found in the .env file will be
# loaded as environment variables
dotenv.load_dotenv()
BILLBOARD_BASE_URL = 'https://www.billboard.com/charts/hot-100'

# SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
# SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
# SPOTIFY_BASE_URL = 'https://api.spotify.com'

date_str = get_date_str()

print('Getting data from Billboard...')
# scrape data from billboard.com
response = requests.get(urljoin(BILLBOARD_BASE_URL, date_str))
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')
list_rows = soup.find_all(name='ul', class_='o-chart-results-list-row')
billboard_week = soup.select_one('.chart-results p').string

# store data to a dictionary
key = f'billboard hot 100 on {billboard_week}'
result = {key: []}
for row in list_rows:
    result[key].append({
        'rank': row.select_one('.o-chart-results-list__item span').string.strip(),
        'track': row.select_one('#title-of-a-story').string.strip(),
        'artist': row.select_one('#title-of-a-story + span').string.strip()
    })

print('Searching songs on Spotify...')
# search for corresponding songs in spotify
# set up Client Credentials flow which provides a higher rate limit than you would with the Authorization Code flow.
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
for song in result[key]:
    q = f'track:{song["track"]} artist:{song["artist"]}'
    search_result = sp.search(q, limit=1)
    try:
        uri = search_result['tracks']['items'][0]['uri']
    except:
        song['uri'] = 'N/A'
    else:
        song['uri'] = uri

with open(f'result on {date_str}.json', 'w') as f:
    json.dump(result, f, indent=4)

# set up Authorization Code Flow
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# get current user's id
current_user_id = sp.me()['id']

print('Creating new playlist...')
# create a new playlist
new_playlist = sp.user_playlist_create(current_user_id, key)
playlist_id = new_playlist['id']

print('Adding songs to the playlist...')
# add the song to the playlist
track_uris = [song['uri'] for song in result[key] if song['uri'] != 'N/A']
sp.playlist_add_items(playlist_id, track_uris)

print(f'Done. {len(track_uris)} songs added.')