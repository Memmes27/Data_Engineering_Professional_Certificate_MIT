# pip install cassandra-driver
from cassandra.cluster import Cluster

# Initialize connection
keyspace = None
cluster = Cluster(['localhost'])
session = cluster.connect(keyspace)

# Create keyspace
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS books 
    WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
""")
session.set_keyspace('books')

# Create table
session.execute("""
    CREATE TABLE IF NOT EXISTS book (
        Book_ID int,
        Name text,
        Author text,
        Year_Published int,
        Number_of_Pages int,
        PRIMARY KEY (Book_ID)
    );
""")

# Insert books
books = [
    (1, 'The Mystery of Capital', 'Hernando de Soto', 1970, 209),
    (2, 'Fairy Tales', 'Hans Christian Andersen', 1836, 784),
    (3, 'The Divine Comedy', 'Dante Alighieri', 1315, 928),
    (4, 'Romeo and Juliet', 'William Shakespeare', 1597, 100)
]

for book in books:
    session.execute("""
        INSERT INTO book (Book_ID, Name, Author, Year_Published, Number_of_Pages)
        VALUES (%s, %s, %s, %s, %s)
    """, book)

print("Books have been inserted successfully!")