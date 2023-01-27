import requests
import time
import json

with open('data.json', 'r') as f:
    data = json.load(f)
    USERNAME = data['username']
    PASSWORD = data['password']
    USER_AGENT = data['useragent']

headers = {
    'User-Agent': USER_AGENT,
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Origin': 'http://172.16.0.30:8090',
    'Connection': 'keep-alive',
    'Referer': 'http://172.16.0.30:8090/',
}

data = {
    'mode': '191',
    'username': USERNAME,
    'password': PASSWORD,
    'a': '1674638802831',
    'producttype': '0',
}

try:
    response = requests.post('http://172.16.0.30:8090/login.xml', headers=headers, data=data)
    print(response)
except Exception:
    print("Wifi down :(")
