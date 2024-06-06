from google.cloud import storage
import os

# define function that uploads a file from the bucket
def upload_lyrics(lyrics:str, destination_file_name:str)->bool: 

    # set key credentials file path
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'./key/gcs.json'
    bucket_name = 'geniuslyrics-km' #km
    # bucket_name = 'geniuslyrics' #aj
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_file_name)
    blob.upload_from_string(lyrics)

    return True

if __name__=="__main__":
    lyrics = 'teeiiiieest!!!'
    destination_file_name = 'test-lyrics.txt'
    print(upload_lyrics(lyrics,destination_file_name))