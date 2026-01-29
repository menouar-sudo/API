import requests
import random
from PIL import Image
from io import BytesIO

import requests

url = "https://pokeapi.co/api/v2/pokemon/"

r = requests.get(url)
data = r.json()
# for key in data.keys():
#   print(key)
# pokemon namesfor i in range(len(data['results'])):print(data['results'][i]['name'])


choice = random.randint(1, len(data['results']))
print(data['results'][choice]['name'])
ulr2 = data['results'][choice]['url']
r2 = requests.get(ulr2)
data2 = r2.json()
for key in data2.keys():
    print(key)
print(data2['sprites']['front_default'])
response = requests.get(data2['sprites']['front_default'], timeout=10)
response.raise_for_status()  # VERY important

img = Image.open(BytesIO(response.content))
img.load()   # force validation
img.show()
