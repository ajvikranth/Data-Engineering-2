from cosume_from_kafka.consume import consume_from_topics
from insert_to_db.insert import insert_track_recommendations,\
      insert_track_analysis, insert_track_details , insert_track_ranks

if __name__=="__main__":
    topics  = ['detail','analysis','recommendations','rank']
    for topic in topics:
        for value in consume_from_topics(topic):
            if value is None:
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
        # print(data)
        # if list(data)[0] == None:
        #     print('no data to consume')
        # if topic == 'detail':
        #     for i in data:
        #         print(i)
        #         x =insert_track_details(i)
        #         if x:
        #             print('track details inserted')
        # elif topic == 'analysis':
        #     for i in data:
        #         x = insert_track_analysis(i)
        #         if x:
        #             print('track analysis inserted')
        # elif topic == 'recommendations':
        #     for i in data:
        #         x=insert_track_recommendations(i)
        #         if x:
        #             print('track recommendation inserted')
        # elif topic == 'rank':
        #     for i in data:
        #         x = insert_track_ranks(i)
        #         if x:
        #             print('track rank inserted')