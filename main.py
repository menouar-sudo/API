
import requests
from PIL import Image
from io import BytesIO
# number at the end of the URL represents the pokemon ID, each set of 4 represents same pokemon
url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"

response = requests.get(url, timeout=10)
response.raise_for_status()  # VERY important

img = Image.open(BytesIO(response.content))
img.load()   # force validation
img.show()
