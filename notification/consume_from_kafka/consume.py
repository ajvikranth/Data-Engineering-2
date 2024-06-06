from kafka import KafkaConsumer
import json 
import time


def consume_from_recomendations():
    consumer = KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False,
    bootstrap_servers='localhost:9094',consumer_timeout_ms=5000)
    consumer.subscribe('recommendations')
    n=0
    for message in consumer:
        n+=1
        try :
            value =  json.loads(message[6].decode('utf-8'))
        except IndexError:
            value =  None
        yield value 