from supabase import create_client, Client
import datetime
from config.config import config

url: str = config['url']
key: str = config['key']

def insert_track_analysis(track_analysis:dict)->bool:

    # track_analysis = list(track_analysis)[0]
    supabase: Client = create_client(url, key)
    data, count = supabase.table('trackanalysis').upsert(track_analysis).execute()
    data, ls = data
    if len(ls)>0:
        return True
    return False

def insert_track_details(track_details:dict)->bool:

    del track_details['rank']

    try:
        datetime.date.fromisoformat((track_details['release_date']))
    except ValueError:
        track_details['release_date'] = None

    supabase: Client = create_client(url, key)
    
    data, count = supabase.table('trackdetails').upsert(track_details).execute()
    data, ls = data
    if len(ls)>0:
        return True
    return False

def insert_track_ranks(ranks:dict)->bool:

    supabase: Client = create_client(url, key)
    
    data, count = supabase.table('ranks').upsert(ranks).execute()
    data, ls = data

    if len(ls)>0:
        return True
    return False

def insert_track_recommendations(recommendations:dict)->bool:
    
    supabase: Client = create_client(url, key)
    
    data, count = supabase.table('recommendations').upsert(recommendations).execute()
    data, ls = data
    if len(ls)>0:
        return True
    return False


if __name__=="__main__":
    track_analysis = {
                'danceability':0.485,
                'energy':0.302,
                'key': 3,
                'loudness':-6.704,
                'mode':1,
                "speechiness":0.101,
                "acousticness":0.768,
                "instrumentalness":0.049,
                "liveness":0.0755,
                "valence":0.246,
                "tempo":160.947,
                "type":'audio_features',
                "id":"17o9JJeBVxQ9O4j50Qd4Vh",
                "duration_ms": 132097
    }

    track_details = {
        'album_name': 'Sequēns',
        'release_date': '2022-12-01',
        'track_in_album': 12,
        'artist_name': 'Archer Marsh', 
        'explicit': False,
        'id': '1o9JJeBKlVxQ9O4j5Qd4Vh', 
        'name': 'Give Me Everything - Stripped Down', 
        'popularity': 62
        }
    ranks = {
        'id': '1o9JJeBKlVxQ9O4j5Qd4Vh',
        'rank':1
    }

    recommendations = {
        'id': '1o9JJeBKlVxQ9O4j5Qd4Vh',
        'recommendations': ['1o9JJeBKlVxQ9O4j5Qd4Vh','1o9JJeBKlVxQ9O4j5Qd4Vh','1o9JJeBKlVxQ9O4j5Qd4Vh','1o9JJeBKlVxQ9O4j5Qd4Vh']
    }
    print(track_analysis)
    print(insert_track_analysis(track_analysis))
    print(insert_track_details(track_details))
    print(insert_track_recommendations(recommendations))
