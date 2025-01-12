import os
import sys

# ----------------
# input arguments
# ----------------
# -create, create containers

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# delete container
def delete(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Deleted {db}')

# read input argument
argument = len(sys.argv)
if (argument > 1):
    argument = sys.argv[1]

# if -create input argument, create containers
if(argument == '-create'):
    # MySQL
    create('docker run -p 3300:3306 --name my_sql -e MYSQL_ROOT_PASSWORD=Egyptiancobra27! -d mysql', 'mysql')

    # MongoDB
    create('docker run -p 27017:27017 --name some-mongo -d mongo', 'mongodb')
    
    # Redis
    create('docker run -p 6379:6379 --name some-redis -d redis', 'redis')
    
    # Cassandra
    create('docker run -p 9042:9042 --name some-cassandra -d cassandra', 'cassandra')

# if -delete input argument, delete containers
elif(argument == '-delete'):
    # MySQL
    delete('docker stop my_sql && docker rm my_sql', 'mysql')

    # MongoDB
    delete('docker stop some-mongo && docker rm some-mongo', 'mongodb')
    
    # Redis
    delete('docker stop some-redis && docker rm some-redis', 'redis')
    
    # Cassandra
    delete('docker stop some-cassandra && docker rm some-cassandra', 'cassandra')