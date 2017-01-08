import json
import requests

url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=da15d37c06066cfd2f782a2758e580b0&format=json'

data = requests.get(url).text
data = json.loads(data)
# print(type(data))
# print(data)
print(data['topartists']['artist'][0]['name'])
