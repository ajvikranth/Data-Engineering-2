from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import time
from config.config import config
from collections.abc import Iterator
from typing import Tuple

SPOTIPY_CLIENT_ID= config['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET=config['SPOTIPY_CLIENT_SECRET']

def get_tracks_from_playlist(playlist_id:str)->Iterator[Tuple[str,int]]:
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET))

        offset = 0
        count = 0
        while True:
            response = sp.playlist_items(playlist_id,
                                        offset=offset,
                                        fields='items.track.id,total',
                                        additional_types=['track'])

            if len(response['items']) == 0:
                break

            for item in response['items']:
                count+=1
                yield item['track']['id'], count

            offset = offset + len(response['items'])

def get_track_details(track_id:str)->dict:
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET))
    track_uri = f'spotify:track:{track_id}'
    time.sleep(1)
    track = sp.track(track_uri)

    required_track_info = {
        'album_name': track['album']['name'],
        'release_date': track['album']['release_date'], 
        'track_in_album': track['album']['total_tracks'],
        'artist_name': track['artists'][0]['name'],
        'explicit': track['explicit'],
        'id': track['id'],
        'name': track['name'],
        'popularity': track['popularity'],
    }

    return required_track_info

if __name__=="__main__":
        for item, count in get_tracks_from_playlist('5nNNZADxLtK4VcC5QWNo0O'):
              print(item, count)