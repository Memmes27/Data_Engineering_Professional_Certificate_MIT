import mysql.connector
from datetime import datetime
import uuid
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(
    user='root', 
    password='root123',
    host='127.0.0.1',
    port=3300,
    database='books'
)

# create cursor
cursor = cnx.cursor()

# insert
query = ("SELECT * FROM favorite_books")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# clean up
cursor.close()
cnx.close()    