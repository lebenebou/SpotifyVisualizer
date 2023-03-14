# SpotifyVisualizer3
Minimalist window that connects to the [Spotify API](https://developer.spotify.com/documentation/web-api/). and shows current playing track aesthetically. Allows for playback controls as well as muting ads for non-premium users. Made with Python using [Tkinter](https://docs.python.org/3/library/tkinter.html).

![Screenshot](https://raw.githubusercontent.com/lebenebou/SpotifyVisualizer3/main/pictures/screenshot.png)

## fetcher.py
Fetches current playback info using the [Spotipy Library](https://spotipy.readthedocs.io/).
Prompts user for authentication with Spotify in a separate browser on the first run.
Fetches current song/playback info as json file and saves it locally in ```playback_data.json```.

## window.py
Constitutes the front-end of the project. One single minimalistic window that shows current playing track artwork with a blurred background.
Contains one [Tkinter Canvas](https://pythonbasics.org/tkinter-canvas/#:~:text=A%20tkinter%20canvas%20can%20be,ovals%2C%20polygons%2C%20and%20rectangles.) that fills up the window, inside of which are 3 pictures, one for the main artwork, one for the blurred background, and one static picture behind the artwork that gives it a drop shadow.
Every 2 seconds, new playback info is fetched and the window is updated to match the data received from the API.

### Keyboard Shortcuts
```<F> or Double Click``` for toggling fullscreen.

```<space>``` for play/pause.

```<left arrow / right arrow>``` for previous/next track.

```<up arrow / down arrow>``` for volume up/down.

## Required Libraries
```pip install pillow```

```pip install spotipy```

```pip install pyautogui```