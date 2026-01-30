import requests
import random
from PIL import Image
from io import BytesIO
from main import *
import requests

url = "https://pokeapi.co/api/v2/pokemon/"

r = requests.get(url)
data = r.json()
# for key in data.keys():
#   print(key)
# pokemon names


print("Welcome to the Game\nWhoOoOoO's That Pokemon")
choice = random.randint(1, len(data['results']))
print(data['results'][choice]['url'])
#print(data['results'][choice]['name'])
ulr2 = data['results'][choice]['url']
r2 = requests.get(ulr2)
data2 = r2.json()
print("it's height is:",data2['height'])
print("it's weight is:",data2['weight'])
print("it's type is:",data2['types'][0]["type"]["name"])
for i in range(len(data['results'])):
    print(data['results'][i]['name'])
#enable the print below if u are too lazy to keep guessing
#print(data['results'][choice]['name'])
while True:
    answer = input("guess the pokemon (or 'q' to quit )")
    if answer == data['results'][choice]['name'] :
        print("yeeey u guessed correct ! ")
        fetch_pokemon_image(data2['sprites']['front_default'])
        break
    elif answer.lower() == 'q':
        break
    else:
        print("better luck next time !")