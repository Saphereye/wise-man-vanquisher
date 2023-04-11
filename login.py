import requests
import json

with open('data.json', 'r') as f:
    data = json.load(f)
    USERNAME = data['username']
    PASSWORD = data['password']

headers = {
    'Origin': 'http://172.16.0.30:8090',
    'Connection': 'keep-alive',
    'Referer': 'http://172.16.0.30:8090/',
}

data = {
    'mode': '191',
    'username': USERNAME,
    'password': PASSWORD,
}

try:
    response = requests.post('http://172.16.0.30:8090/login.xml', headers=headers, data=data)
    print(response)
except Exception:
    print("Wifi down :(")
