import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import dotenv

dotenv.load_dotenv()


search_str = 'track:Doxy artist:Miles Davis'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str, limit=1)
pprint.pprint(result)