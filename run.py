import spotipy
import random
import requests
import string
import urllib
import os
from spotipy.oauth2 import SpotifyClientCredentials
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def run():
    # Get random artist   
    wildcard = f'%{random.choice(string.ascii_lowercase)}%'
    query = urllib.parse.quote(wildcard)
    offset = random.randint(0, 2000)
    artist_profile = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=artist'

    response = requests.get(
        artist_profile,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('SPOTIFY_AUTH_TOKEN')}"
        }
    )
    response_json = response.json()

    artist_profile = response_json['artists']['items']
    artist_name = artist_profile[0]['name']
    artist_url = artist_profile[0]['external_urls']['spotify']
    artist_followers = artist_profile[0]['followers']['total']
    print(f'Artist: {artist_name}')
    print(f'Followers: {artist_followers}')
    print(f'Link: {artist_url}')

    # Get artist's top 5 songs
    top_songs = spotify.artist_top_tracks(artist_url)

    # Give links to previews of each song
    for song in top_songs['tracks'][:5]:
        if song['preview_url']:
            print('Song    : ' + song['name'])
            print('Audio    : ' + song['preview_url'])
            print()
        else:
            print('No preview available')

if __name__ == '__main__':
    run()
