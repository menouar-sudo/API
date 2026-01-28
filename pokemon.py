from pprint import pprint
import requests
from fastapi import FastAPI


url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)

data = response.json()
keys = data.keys()
for key in keys:
    print(key)


pprint(data["abilities"])
