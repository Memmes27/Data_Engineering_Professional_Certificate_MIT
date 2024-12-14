import mysql.connector
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(
    user='root', 
    password='root123',
    host='127.0.0.1',
    port=3300,
    auth_plugin='mysql_native_password'
)

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `books`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS books")
cursor.execute(query)

# use db
query = ("USE books")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE favorite_books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    year_published INT
)
''')
cursor.execute(query)

# insert initial data
books = [
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    ("1984", "George Orwell", 1949),
    ("To Kill a Mockingbird", "Harper Lee", 1960)
]

for book in books:
    query = ("INSERT INTO favorite_books (title, author, year_published) VALUES (%s, %s, %s)")
    cursor.execute(query, book)

# clean up
cnx.commit()
cursor.close()
cnx.close()