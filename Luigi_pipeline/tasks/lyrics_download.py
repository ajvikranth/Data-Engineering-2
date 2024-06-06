import luigi
from api.genius import get_lyrics
from gcs.upload_file import upload_lyrics

class LyricsDownload(luigi.Task):
    track_details = luigi.DictParameter()
    uploaded = False

    def run(self):
        lyrics = get_lyrics(self.track_details)
        track_id = lyrics['id']
        file_path = f'{track_id}-lyrics.txt'
        self.uploaded = upload_lyrics(str(lyrics['lyrics']).encode('utf-8'),file_path)
    
    def complete(self):
        return self.uploaded
    
    





        
