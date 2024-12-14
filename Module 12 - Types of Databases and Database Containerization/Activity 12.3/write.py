# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# write to server using mset
r.mset({
    'Italy': 'Rome',
    'France': 'Paris'
})