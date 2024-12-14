# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# read items using get
print("Capital of Italy:", r.get('Italy'))
print("Capital of France:", r.get('France'))