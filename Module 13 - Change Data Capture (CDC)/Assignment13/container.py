import os
import sys
import pymysql
from cassandra.cluster import Cluster
import time

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# delete container
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# initialize mysql db
def init_mysql():
    cnx = pymysql.connect(user='root', 
        password='Egyptiancobra27!',
        host='127.0.0.1',
        port=5600)

    cursor = cnx.cursor()
    cursor.execute("DROP DATABASE IF EXISTS `pluto`;")
    cursor.execute("CREATE DATABASE IF NOT EXISTS pluto")
    cursor.execute("USE pluto")
    cursor.execute('''
    CREATE TABLE posts(
        id VARCHAR(36),
        stamp VARCHAR(20)
    )
    ''')
    cnx.commit()
    cursor.close()
    cnx.close()
    print("MySQL initialized!")

# initialize cassandra db
def init_cassandra():
    try:
        keyspace = None
        cluster = Cluster(['localhost'], port=1000)
        session = cluster.connect(keyspace)

        session.execute("""
            CREATE KEYSPACE IF NOT EXISTS stamps
            WITH REPLICATION = {'class':'SimpleStrategy','replication_factor':1};
            """)

        session.set_keyspace('stamps')
        session.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id text PRIMARY KEY,
                stamp text
            );
            """)

        session.execute("insert into posts (id, stamp) values ('maxTimeStamp', '1975-01-01 00:00:00') IF NOT EXISTS")
        print("Cassandra initialized!")
    except Exception as e:
        print(f"Error initializing Cassandra: {e}")

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('final_mysql_container')
    delete('final_mongo_container')
    delete('final_redis_container')
    delete('final_cassandra_container')
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 5600:3306 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=Egyptiancobra27! -d mysql', 'mysql')
    create('docker run -p 1800:27017 --name final_mongo_container -d mongo', 'mongodb')
    create('docker run -p 2400:6379 --name final_redis_container -d redis', 'redis')
    create('docker run -p 1000:9042 --name final_cassandra_container -d cassandra', 'cassandra')
    print("Waiting for containers to start...")
    time.sleep(10)
    sys.exit()

# if -init, init mysql and cassandra
if(argument == '-init'):
    time.sleep(15)  # Wait for containers to be fully ready
    init_mysql()
    init_cassandra()
    sys.exit()