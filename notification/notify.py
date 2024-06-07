from api.spotify import get_tracks_from_playlist, get_track_details
from consume_from_kafka.consume import consume_from_recomendations
from db.utils import select, create_table
from send_email.send_email import send_email

if __name__=="__main__":
    conn = create_table()
    sent = False
    for email,playlist_id in select(conn):

        tracks_in_playlist = list(get_tracks_from_playlist(playlist_id))
        tracks_in_playlist = [track for track,i in tracks_in_playlist]
        print(tracks_in_playlist)
        for recommendations in consume_from_recomendations():
            print(recommendations)
            for track in recommendations['recommendations']:
                print(track in tracks_in_playlist)
                if track in tracks_in_playlist:
                    track_details = get_track_details(recommendations['id'])
                    send_email(email,track_details)
                    sent = True
                    break
            if sent:
                break
            



