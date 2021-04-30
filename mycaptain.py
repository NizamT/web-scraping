import sqlite3
def connect(dmname):
    conn = sqlite3.connect(dmname)

    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE TEXT, AMENITIES TEXT, RATING TEXT")
    print("Table created sucessfully!")
    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    print("Inserted into table: " + str(values))
    insert_sql = "INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENTITIES, RATING) VALUES (?, ?, ?, ?, ?)"

    conn.execute(insert_sql,values)

    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn = sqlite3.connect(dbname)