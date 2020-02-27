#using python to call api's using a free api ()

import requests
import json

base_url = 'https://api.upcitemdb.com/prod/trial/lookup'

parameters = {'upc' : '073366118238'}

response = requests.get(base_url, params=parameters)

# Testing thye url building
print(response.url)

# data comes as JSON, which is not built into python
# need to import a package, using json module
content = response.content

info = json.loads(content)

# see what type of reponse
#print(type(info))
#print(info)

# getting the data we want
item = info['items']

item_info = item[0]

title = item_info['title']

brand = item_info['brand']

print(title)
print(brand)