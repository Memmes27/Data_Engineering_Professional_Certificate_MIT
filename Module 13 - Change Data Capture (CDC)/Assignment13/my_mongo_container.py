import os
import sys

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 1800:27017 --name final_mongo_container -d mongo', 'mongodb')