import sqlite3
from sqlite3 import Error

def create_table()->sqlite3.Connection:
    db_path = 'notify.db'
    conn = sqlite3.connect(db_path)
    
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS notification_record (
            email text PRIMARY KEY,
            playlist_id text 
        );
        """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)
    return conn

def insert(conn:sqlite3.Connection,email:str, play_list:str)->bool:
    sql = ''' INSERT INTO notification_record(email,playlist_id)
              VALUES(?,?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, (email,play_list))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
    
def select(conn:sqlite3.Connection):
    sql = ''' SELECT * FROM notification_record;'''
    try:
        cur = conn.cursor()
        data = cur.execute(sql)

        return data.fetchall()
    except Error as e:
        print(e)
        return None