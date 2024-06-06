import sqlite3
from sqlite3 import Error

def create_table()->sqlite3.Connection:
    db_path = 'tracks.db'
    conn = sqlite3.connect(db_path)
    
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS track_record (
            track_id text PRIMARY KEY,
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)
    return conn

def insert(conn:sqlite3.Connection, track_id:str)->bool:
    sql = ''' INSERT INTO track_record(track_id)
              VALUES(?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, (track_id,))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False

if __name__=="__main__":
    conn = create_table()
    track_id = '1o9JJeBKlVxQ9O4j5Qd4Vh'
    print(insert(conn,track_id))
