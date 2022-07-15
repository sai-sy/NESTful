import requests
import json

BASE = "http://api.saiscripts.com/"

ON = "https://represent.opennorth.ca/"

payload = {"email": "saihaansyedprofiles@gmail.com", "postal_code": "M1L 3G6"}
response = requests.post(BASE + 'persons/email/saihaansyedprofiles@gmail.com', json=payload)

print(response.text)
