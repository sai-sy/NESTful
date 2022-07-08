import requests
import json

BASE = "http://127.0.0.1:5000/"

payload = {"likes": 10, "views": 50, "name": "krish one kiss dance"}

response = requests.get(BASE + 'videos/1', json=payload)

print(response.json())