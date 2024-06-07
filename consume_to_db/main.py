from cosume_from_kafka.consume import consume_from_topics
from insert_to_db.insert import insert_track_recommendations,\
      insert_track_analysis, insert_track_details , insert_track_ranks

if __name__=="__main__":
    topics  = ['detail','analysis','recommendations','rank']
    for topic in topics:
        for value in consume_from_topics(topic):
            if value is None:
                print("no track to insert")
                break
            if topic == 'detail':
                x =insert_track_details(value)
                if x:
                    print('track details inserted')
            if topic == 'analysis':
                x =insert_track_analysis(value)
                if x:
                    print('track analysis inserted')
        
            if topic == 'recommendations':
                x =insert_track_recommendations(value)
                if x:
                    print('track recomendation inserted')
            if topic == 'rank':
                x =insert_track_ranks(value)
                if x:
                    print('track rank inserted')            
