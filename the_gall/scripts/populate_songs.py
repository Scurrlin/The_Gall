import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import math

load_dotenv()

# Fetch Spotify API credentials from environment variables
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Authenticate with Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define your list of songs
songs = [
    {'title': "99 Problems", 'artist': "Hugo"},
    {'title': "Too Sweet", 'artist': "Hozier"},
    {'title': "Sleep On The Floor", 'artist': "The Lumineers"},
    {'title': "Steady, As She Goes", 'artist': "The Raconteurs"},
    {'title': "Midnight Train To Memphis", 'artist': "Chris Stapleton"},
    {'title': "Feels Like Summer", 'artist': "Childish Gambino"},
    {'title': "Keep on Loving You", 'artist': "REO Speedwagon"},
    {'title': "Believe", 'artist': "Cher"},
    {'title': "War Pigs", 'artist': "Black Sabbath"},
    {'title': "Northern Attitude", 'artist': "Noah Kahan"},
    {'title': "Mess", 'artist': "Noah Kahan"},
    {'title': "Ball and Biscuit", 'artist': "The White Stripes"},
]

# Iterate over each song
for i, song_data in enumerate(songs, start=1):
    # Search for the song on Spotify
    results = sp.search(q=f"track:{song_data['title']} artist:{song_data['artist']}", type='track', limit=1)

    # Check if search returned any results
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        # Extract song details
        title = track['name']
        artist = track['artists'][0]['name']
        thumbnail_url = track['album']['images'][0]['url']
        playback_url = track['external_urls']['spotify']
        duration_ms = track['duration_ms']

        # Print song details
        print(f"{i}. {title} - {artist}")
        print(f"   Thumbnail URL: {thumbnail_url}")
        print(f"   Playback URL: {playback_url}")
        print(f"   Duration: {duration_ms} ms")
        for track in results:
            time = math.floor(duration_ms / 1000)
            timeM = math.floor(time / 60)
            timeS = math.floor(time % 60)
            print(str(timeM) + ":" + str(timeS))
    else:
        # Handle case where song was not found on Spotify
        print(f"{i}. Song '{song_data['title']}' by '{song_data['artist']}' not found on Spotify")