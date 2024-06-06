from db.utils import create_table, insert

if __name__=="__main__":
    conn = create_table()
    print(insert(conn,'antonvikranth@gmail.com','6FYKn1CjyjFg7wU1SR5Vb7'))