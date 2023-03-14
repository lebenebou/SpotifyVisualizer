
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# ===========================================================
with open("credentials.json", "r") as f: creds = json.load(f)
scopes = "user-read-playback-state"
id, secret, uri = creds["client_id"], creds["client_secret"], creds["redirect_uri"]

manager_object = SpotifyOAuth(client_id=id, client_secret=secret, redirect_uri=uri, scope=scopes)
sp_object = spotipy.Spotify(auth_manager=manager_object)
# ===========================================================

def fetch_playback_info() -> None:

    playback_info = None

    try:
        playback_info = sp_object.current_playback()
    except:
        with open("./playback_data.json", "w") as f: json.dump({"message":"no_internet"}, f)
        return

    if playback_info==None:
        with open("./playback_data.json", "w") as f: json.dump({"message":"spotify_closed"}, f)
        return

    with open("./playback_data.json", "w") as f: json.dump(playback_info, f)


if __name__=="__main__":

    # on the first ever call of this function, user will be prompeted to sign in in the browser
    fetch_playback_info()