import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

def get_spotify_client():
    scope = (
      "user-read-playback-state "
      "user-modify-playback-state "
      "user-read-currently-playing "
      "playlist-read-private"
    )
    return spotipy.Spotify(
      auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=scope
      )
    )
