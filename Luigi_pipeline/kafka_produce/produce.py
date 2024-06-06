from kafka import KafkaProducer
import json

def produce(topic:str ,data:dict)->bool:

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'],value_serializer=lambda m: json.dumps(m).encode('ascii'))
    try:

        if topic == 'detail':
            producer.send(topic='detail',value=data)
        elif topic == 'analysis':
            producer.send(topic='analysis',value=data)
        elif topic == 'recommendations':
            producer.send(topic='recommendations',value=data)
        elif topic == 'rank':
            producer.send(topic='rank', value= data)
        return True
    
    except Exception as e:
        print(e)
        return False
    
if __name__=="__main__":
    track_detail = {
        'rank':1,
        'album_name': 'Sequēns',
        'release_date': '2022-12-01',
        'track_in_album': 12,
        'artist_name': 'Archer Marsh', 
        'explicit': False,
        'id': '1o9JJeBKlVxQ9O4j5Qd4Vh', 
        'name': 'Give Me Everything - Stripped Down', 
        'popularity': 62
        }
    print(produce('detail',track_detail))

    