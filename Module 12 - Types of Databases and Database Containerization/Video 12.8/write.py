# pip install cassandra-driver
from cassandra.cluster import Cluster
from datetime import datetime

keyspace = None
cluster = Cluster(['localhost'])
session = cluster.connect(keyspace)

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS pluto 
    WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
""")
session.set_keyspace('pluto')

session.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        bucket varchar,
        stamp text,
        PRIMARY KEY (bucket, stamp)
        ) WITH CLUSTERING ORDER BY (stamp desc);
""")

stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
session.execute(f"""
    INSERT INTO posts (bucket, stamp) 
    VALUES ('timeloop','{stamp}');
""")
