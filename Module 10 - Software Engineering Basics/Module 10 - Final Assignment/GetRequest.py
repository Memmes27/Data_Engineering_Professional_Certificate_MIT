import http.client
import json

conn = http.client.HTTPConnection("localhost", 1337)
payload = ''
headers = {
  'Content-Type': 'application/json'
}
conn.request("GET", "/api/flights", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))