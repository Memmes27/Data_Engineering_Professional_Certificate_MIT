
import os
import sys
import pymysql
from cassandra.cluster import Cluster
import time


# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers
# -init, init mysql, mongodb does not need it

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')


def wait_for_cassandra():
    max_attempts = 30  # wait up to 30 seconds
    for attempt in range(max_attempts):
        try:
            cluster = Cluster(['localhost'], port=9042)
            session = cluster.connect()
            print("Cassandra is ready!")
            cluster.shutdown()
            return True
        except Exception as e:
            print(f"Waiting for Cassandra to start... ({attempt + 1}/{max_attempts})")
            time.sleep(1)
    return False

# initialize cassandra db
def init_cassandra():
    if not wait_for_cassandra():
        print("Cassandra failed to start in time")
        return
        
    keyspace = None
    cluster = Cluster(['localhost'], port=9042)
    session = cluster.connect(keyspace)

    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS stamps
        WITH REPLICATION = {'class':'SimpleStrategy','replication_factor' :1};
        """)

    session.set_keyspace('stamps')
    session.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id text  PRIMARY KEY,
            stamp text
        );
        """)

    session.execute(f"insert into posts (id, stamp) values ('maxTimeStamp', '1975-01-01 00:00:00') IF NOT EXISTS")

# initialize mysql db
def init_mysql():
    cnx = pymysql.connect(user='root', 
        password='Egyptiancobra27!',
        host='127.0.0.1')

    # create cursor
    cursor = cnx.cursor()

    # delete previous db
    query = ("DROP DATABASE IF EXISTS `pluto`;")
    cursor.execute(query)

    # create db
    query = ("CREATE DATABASE IF NOT EXISTS pluto")
    cursor.execute(query)

    # use db
    query = ("USE pluto")
    cursor.execute(query)

    # create table
    query = ('''
    CREATE TABLE posts(
        id VARCHAR(36),
        stamp VARCHAR(20)
    )
    ''')
    cursor.execute(query)

    # clean up
    cnx.commit()
    cursor.close()
    cnx.close()    

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('some-mysql')
    delete('some-mongo')
    delete('some-redis')  # Added for Redis
    delete('some-cassandra')
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=Egyptiancobra27! -d mysql', 'mysql')
    create('docker run -p 27017:27017 --name some-mongo -d mongo', 'mongo')
    create('docker run -p 6379:6379 --name some-redis -d redis', 'redis')  # Added for Redis
    create('docker run -p 9042:9042 --name some-cassandra -d cassandra', 'cassandra')
    sys.exit()

# if -init, init mysql, mongodb does not need it
if(argument == '-init'):
    init_mysql()
    init_cassandra()
    sys.exit()
