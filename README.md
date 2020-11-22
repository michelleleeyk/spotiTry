# spotiTry
Discover new artists efficiently and effectively. This program generates a random artist and allows users to listen to short previews of their top 5 songs. </br>


## to run:
1. Define environment variables
export SPOTIPY_CLIENT_ID='0ec3ea24eb5d47c99376094d95e9a79d'
export SPOTIPY_CLIENT_SECRET='2505badcf39d4ebc9d897ff1a2746e2d'
export SPOTIFY_AUTH_TOKEN=(your token from the Search for an Item (https://developer.spotify.com/console/get-search-item/?q=m&type=artist&market=&limit=1&offset=203&include_external=), without apostrophes)
python song_preview.py
# *** note: it's spotiPy client id!!! 

# future plans
    # option to follow artist
    # spotify.user_follow_artists(artist['id'])

    # option to add song to library 
    # current_user_saved_tracks_add(tracks=None)

    # get number of streams of song
