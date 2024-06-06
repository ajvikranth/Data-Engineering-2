from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from collections.abc import Iterator
import time
from typing import Tuple
from  config.config import config


SPOTIPY_CLIENT_ID= config['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET=config['SPOTIPY_CLIENT_SECRET']


def get_viral_50()->Iterator[Tuple[str,int]]:

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET))

    pl_id = 'spotify:playlist:37i9dQZEVXbLiRSasKsNU9'
    offset = 0
    rank = 0
    while True:
        response = sp.playlist_items(pl_id,
                                    offset=offset,
                                    fields='items.track.id,total',
                                    additional_types=['track'])

        if len(response['items']) == 0:
            break

        for item in response['items']:
            rank+=1
            yield item['track']['id'], rank

        offset = offset + len(response['items'])


def get_track_analysis(track_id:str)->dict:
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET))

    track_uri = f'spotify:track:{track_id}'
    time.sleep(1)
    features = sp.audio_features(track_uri)[0]

    unwanted_features = ["time_signature","analysis_url","track_href","uri"]

    return {k: features[k] for k in features.keys() if k not in unwanted_features }


def get_track_details(track_id:str, rank:int=-1)->dict:
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET))
    track_uri = f'spotify:track:{track_id}'
    time.sleep(1)
    track = sp.track(track_uri)

    required_track_info = {
        'rank': rank,
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


def get_recomendation(track_id:str)->list:

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET))
    time.sleep(1)
    tracks = sp.recommendations(seed_tracks=[track_id],
                                        limit=5)['tracks']
    recommended_track_ids = []
    for track in tracks:
        recommended_track_ids.append(track['id'])
    
    recommendations = {
        'id': track_id,
        'recommendations': recommended_track_ids
    }

    return recommendations
    

if __name__=="__main__":
    n = 0
    for track_id,rank in get_viral_50():
        print(track_id)
        print(get_track_analysis(track_id))
        print(get_track_details(track_id,rank))
        print(get_recomendation(track_id))
        n+=1
        if n==1:
            break
