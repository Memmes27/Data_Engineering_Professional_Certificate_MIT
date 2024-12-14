from cassandra.cluster import Cluster

cluster = Cluster(['localhost'],port=9042)
session = cluster.connect('pluto',wait_for_all_pools=True)
session.execute('USE pluto')
rows = session.execute('SELECT * FROM posts')
for row in rows:
    print(row)
