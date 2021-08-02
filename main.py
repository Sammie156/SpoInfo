from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Fetching CLIENT_ID and CLIENT_SECRET from the `.env` file, not pushed
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config('CLIENT_ID'),
                                                           client_secret=config('CLIENT_SECRET')))
while(True):
    choice = input("Enter your choice \n 1. Artists \n 2. Songs \n Quit to Exit \n ")

    if choice.lower() == "Artists":
        while (True):
            name = input("Enter name of Artist : ")
            if name.lower() == "quit":
                break
            # Prints the top ten tracks of the Artist name entered.
            results = sp.search(q=name, type='artist')
            for idx, track in enumerate(results['artists']['items']):
                artist_name = track['name']
                if(artist_name == name):
                    artist_id = track['id']
                    artist = sp.artist(artist_id)
                    artist_uri = artist['uri']
                    popularity = artist['popularity']
                    print(f"ID : {artist_id} \nPopularity : {popularity} \nURI : {artist_uri}\n")

    elif choice == "Songs":
        while(True):
            name = input("Enter name of song : ")
            if name.lower() == "quit":
                break
            results = sp.search(q=name, type='track')
            for idx, track in enumerate(results['tracks']['items']):
                track_name = track['name']
                if(name.lower() == track_name.lower()):
                    track_id = track['id']
                    album_id = track['album']['id']
                    album_name = track['album']['name']
                    song_uri = track['uri']
                    album_uri = track['album']['uri']
                    print(f"Album ID : {album_id} \nSong URI : {song_uri} \nAlbum Name : {album_name}\nAlbum URI : {album_uri}\n")
                    
    elif choice.lower() == "quit":
        print()
        break

