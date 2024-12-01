import http.client
import json

conn = http.client.HTTPConnection("localhost", 3000)
payload = json.dumps({
  "id": 4,
  "name": "Dishdash"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/restaurant", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))