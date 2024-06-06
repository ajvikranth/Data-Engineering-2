from kafka import KafkaConsumer
import json 
import time


def consume_from_topics(topic):
    consumer = KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False,
    bootstrap_servers='localhost:9094',consumer_timeout_ms=5000)
    consumer.subscribe(topic)
    n=0
    for message in consumer:
        # time.sleep(1)
        n+=1
        try :
            value =  json.loads(message[6].decode('utf-8'))
        except IndexError:
            value =None

        yield value 

        # if n>1:
        #     break
    
if __name__=="__main__":
    print(consume_from_topics('rank'))

