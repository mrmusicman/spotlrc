import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import * #put in cid and secret as two variables in a file called config.py with your API keys


client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def apiTrackToNormal(dc):
    return [dc['id'], dc['name'], dc['artists'][0]['name'], dc['album']['images'][0]['url']]
