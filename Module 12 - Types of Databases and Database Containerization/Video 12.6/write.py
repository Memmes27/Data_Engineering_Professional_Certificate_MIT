# pip install pymongo
from pymongo import MongoClient
from datetime import datetime
import uuid

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get database
db = client.pluto

# get collection
posts = db.posts

# document
id = str(uuid.uuid4())
stamp = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
item = {
    'id': id,    
    'stamp': stamp
}

# insert document
db.posts.insert_one(item)