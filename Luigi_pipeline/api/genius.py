from lyricsgenius import Genius
from config.config import config

token = config['gl_token']

def get_lyrics(track_info:dict)->dict:
    genius = Genius(token)
    song = genius.search_song(title=track_info['name'],
                              artist=track_info['artist_name'])
    if song is None:
        lyrics = None
    else:
        lyrics = song.lyrics

    lyrics_res = {
        'id': track_info['id'],
        'lyrics': lyrics,
    }
    
    return lyrics_res


if __name__=="__main__":
    track_info = {
        'album_name': 'Sequēns',
        'release_date': '2022-12-01',
        'track_in_album': 12,
        'artist_name': 'Archer Marsh', 
        'explicit': False,
        'id': '1o9JJeBKlVxQ9O4j5Qd4Vh', 
        'name': 'Give Me Everything - Stripped Down', 
        'popularity': 62
        }
    print(get_lyrics(track_info))