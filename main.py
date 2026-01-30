
import requests
from PIL import Image
from io import BytesIO
# number at the end of the URL represents the pokemon ID, each set of 4 represents same pokemon
def fetch_pokemon_image(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # VERY important
    img = Image.open(BytesIO(response.content))
    img.load()   # force validation
    img.show()
