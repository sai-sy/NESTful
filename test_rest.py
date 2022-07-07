import requests
import json

BASE = "http://127.0.0.1:5000/"

payload = {"likes": 10, "views": 50, "name": "krish one kiss dance"}

headers = {'accept:': 'application/json'}
response = requests.put(BASE + 'video/1', json=payload)

print(response.json())