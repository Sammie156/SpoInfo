from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Fetching CLIENT_ID and CLIENT_SECRET from the `.env` file, not pushed
API_ID = config('CLIENT_ID')
API_SECRET = config('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=API_ID,
                                                           client_secret=API_SECRET))

name = input("Enter Artist name : ")

# Prints the top ten tracks of the Artist name entered.

results = sp.search(q=name, limit=10)
for idx, track in enumerate(results['tracks']['items']):
    print(idx + 1, track['name'])
