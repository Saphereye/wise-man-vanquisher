import requests
import json

with open('data.json', 'r') as f:
    data = json.load(f)
    USERNAME = data['username']

headers = {
    'Origin': 'http://172.16.0.30:8090',
    'Connection': 'keep-alive',
    'Referer': 'http://172.16.0.30:8090/',
}

data = {
    'mode': '193',
    'username': USERNAME,
    'producttype': '0',
}

try:
    response = requests.post('http://172.16.0.30:8090/logout.xml', headers=headers, data=data)
    print(response)
except Exception:
    print("Wifi down :(")
