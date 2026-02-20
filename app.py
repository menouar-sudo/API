import random
from pokedex.repositories import (
    PokemonRepository,
    APIPokemonRepository,
    PokemonInfo,
    MockPokemonRepository,
)
import requests
from PIL import Image
from io import BytesIO


class Pokedex:
    def __init__(self, repository: PokemonRepository):
        self._repository = repository

    def run(self):
        print("Welcome to the Game\nWhoOoOoO's That Pokemon")

        pokemons = self._repository.fetch_all_pokemons()

        choice = random.choice(pokemons)
        pokemon_info = self._repository.fetch_pokemon_info(choice["id"])
        print("_" * 50)
        self.print_pokemon_info(pokemon_info)

        print("_" * 50)
        self.print_pokemon_choices(pokemons)

        self.collect_answer(pokemon_info)

    def print_pokemon_info(self, pokemon: PokemonInfo):
        print("it's height is:", pokemon.height)
        print("it's weight is:", pokemon.weight)
        print("it's type is:", pokemon.type)

    def print_pokemon_choices(self, pokemons: list[dict]):
        print("Choices:")
        for pokemon in pokemons:
            print(pokemon["name"])

    def collect_answer(self, pokemon_info: PokemonInfo):
        while True:
            answer = input("guess the pokemon (or 'q' to quit )")
            if answer == pokemon_info.name:
                print("yeeey u guessed correct ! ")
                self.fetch_image(pokemon_info.image)
                break
            elif answer.lower() == "q":
                break
            else:
                print("better luck next time !")

    def fetch_image(self, url: str):
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # VERY important
        img = Image.open(BytesIO(response.content))
        img.load()  # force validation
        img.show()


api_repository = APIPokemonRepository()
mock_repository = MockPokemonRepository()

app = Pokedex(repository=mock_repository)

app.run()
