from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Fetching CLIENT_ID and CLIENT_SECRET from the `.env` file, not pushed
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config('CLIENT_ID'),
                                                           client_secret=config('CLIENT_SECRET')))

choice = input("Enter your choice \n 1. Artists \n 2. Songs \n")

if choice == "Artists":
    name = input("Enter name of Artist : ")
    # Prints the top ten tracks of the Artist name entered.
    results = sp.search(q=name, type='artist')
    for idx, track in enumerate(results['artists']['items']):
       artist_name = track['name']
       if(artist_name == name):
           artist_id = track['id']
           print("ID :", artist_id)
           artist = sp.artist(artist_id)
           artist_uri = artist['uri']
           popularity = artist['popularity']
           print("Popularity :", popularity)
           print("URI : ", artist_uri)

elif choice == "Songs":
    name = input("Enter name of song : ")
    results = sp.search(q=name, type='track')
    for idx, track in enumerate(results['tracks']['items']):
        track_name = track['name']
        if(name == track_name):
            track_id = track['id']
            album_id = track['album']['id']
            print("Album ID :", album_id)
            print("Album URI : ", track['uri'])
            album_tracks = sp.album_tracks(album_id, limit=10, market='US')
