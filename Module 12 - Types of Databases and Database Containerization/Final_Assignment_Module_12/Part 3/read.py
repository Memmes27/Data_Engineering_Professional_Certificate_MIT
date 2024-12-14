# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# read items using get
print("Value for Milk:", r.get('Milk').decode('utf-8'))
print("Value for Bread:", r.get('Bread').decode('utf-8'))