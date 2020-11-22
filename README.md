# spotiTry
A program that allows users to discover new artists effectively (listen to their most popular songs) and efficiently (listen to 30 second previews of each song).
First, a random artist is generated. Their name, number of followers and top 5 songs will be displayed. Finally, links to the previews of each song are displayed. </br></br>
Created using the [Spotify Web API](https://developer.spotify.com/documentation/web-api/) and [Spotipy library](https://spotipy.readthedocs.io/en/2.16.1/).

## To Run Program
1. Define environment variables </br>
`export SPOTIPY_CLIENT_ID=your_client_id_here` </br>
`export SPOTIPY_CLIENT_SECRET=your_client_secret_here` </br>
`export SPOTIFY_AUTH_TOKEN=your_token_here`</br>
Get your OAuth token [here](https://developer.spotify.com/console/get-search-item/?q=m&type=artist&market=&limit=1&offset=203&include_external=)
</br></br>

2. In terminal </br>
`python run.py`
</br></br>
## Future Plans
* Develop a web app with a simple UI for this program - using Flask, HTML, CSS
* Add user log-in system
* Give users the option to follow the artist (using spotify.user_follow_artist(artist[id'])
* Give users the option to add full song to their library (using spotify.current_user_sved_tracks(tracks=None))
