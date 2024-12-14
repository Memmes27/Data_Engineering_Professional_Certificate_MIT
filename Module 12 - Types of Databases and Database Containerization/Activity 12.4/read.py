from cassandra.cluster import Cluster

# Connect to the cluster
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect('books', wait_for_all_pools=True)

# Select and print all books
rows = session.execute('SELECT * FROM book')
for row in rows:
    print(f"Book ID: {row.book_id}")
    print(f"Name: {row.name}")
    print(f"Author: {row.author}")
    print(f"Year Published: {row.year_published}")
    print(f"Number of Pages: {row.number_of_pages}")
    print("-" * 50)