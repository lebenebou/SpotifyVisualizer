# SpotifyVisualizer3
Minimalist window that connects to Spotify and shows current playing track aesthetically. Allows for playback controls as well as muting ads for non-premium users.

![Screenshot](https://raw.githubusercontent.com/lebenebou/SpotifyVisualizer3/main/pictures/screenshot.png)

## fetcher.py
Fetches current playback info using the [Spotipy Library](https://spotipy.readthedocs.io/).
Prompts user for authentication with Spotify in a separate browser on the first run.
Fetches song info as json file and saves it in local storage.