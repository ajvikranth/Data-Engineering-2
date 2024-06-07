import luigi
from datetime import date
from db.utils import create_table, insert
from api.spotify import get_viral_50, get_track_analysis \
                       ,get_track_details, get_recomendation

from tasks.lyrics_download import LyricsDownload
from tasks.produce_to_kafka import KafkaProduce

class fetch_track_info(luigi.Task):

    conn = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = create_table()

    def requires(self):
        n=0
        for track_id,rank in get_viral_50():
            n+=1
            track_rank = {
                'id': track_id,
                'rank': rank
            }
            yield KafkaProduce(topic='rank',data = track_rank)

            if insert(track_id=track_id,conn=self.conn):
                track_details = get_track_details(track_id,rank)
                track_analysis = get_track_analysis(track_id)
                recommendations = get_recomendation(track_id)

                yield LyricsDownload(track_details)
                yield KafkaProduce(topic='detail',data = track_details)
                yield KafkaProduce(topic='recommendations',data = recommendations)
                yield KafkaProduce(topic='analysis',data = track_analysis)

                for recommended in recommendations['recommendations']:
                    if insert(track_id=recommended,conn=self.conn):
                        r_track_details = get_track_details(recommended)
                        r_track_analysis = get_track_analysis(recommended)

                        yield KafkaProduce(topic='detail',data = r_track_details)
                        yield KafkaProduce(topic='analysis',data = r_track_analysis)

            # if n>=1:
            #     break



    