import requests

import re

import requests

response = requests.get('https://www.melon.com/chart/index.htm')

with open('melon.html', 'w') as f:
    f.write(response.text)

source = open('melon.html', 'r').read()

print(source)
