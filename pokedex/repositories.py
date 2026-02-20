from dataclasses import dataclass
import requests
from abc import ABC, abstractmethod


@dataclass
class PokemonInfo:
    id: int
    name: str
    type: str
    weight: int
    height: int
    image: str


class PokemonRepository(ABC):
    @abstractmethod
    def fetch_all_pokemons(self) -> list[dict]: ...

    @abstractmethod
    def fetch_pokemon_info(self, id: int) -> dict: ...


class APIPokemonRepository(PokemonRepository):
    BASE_URL = "https://pokeapi.co/api/v2"

    def fetch_all_pokemons(self) -> list[dict]:
        url = self.BASE_URL + "/pokemon/"

        r = requests.get(url)
        data = r.json()

        data = [{"id": i} | p for i, p in enumerate(data["results"], start=1)]

        return data

    def fetch_pokemon_info(self, id: int) -> PokemonInfo:
        base_url = self.BASE_URL + "/pokemon/"

        r = requests.get(base_url + str(id))

        data = r.json()

        pokemon = PokemonInfo(
            id=id,
            name=data["name"],
            type=data["types"][0]["type"]["name"],
            weight=data["weight"],
            height=data["height"],
            image=data["sprites"]["front_default"],
        )

        return pokemon


class MockPokemonRepository(PokemonRepository):
    MOCK_DATA = [
        PokemonInfo(
            **{
                "id": 1,
                "name": "toufik",
                "type": "parkingeur",
                "weight": "2",
                "height": "180",
                "image": "https://i1.sndcdn.com/avatars-0cUQN6RpbCELMUDH-roVDew-t240x240.jpg",
            }
        ),
        PokemonInfo(
            **{
                "id": 2,
                "name": "rachid",
                "type": "7itist",
                "weight": "3",
                "height": "140",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvI_wueMFbssyy3RcGwINO5Jn9eipAlVYv0w&s",
            }
        ),
    ]

    def fetch_all_pokemons(self) -> list[dict]:
        return [{"id": p.id, "name": p.name} for p in self.MOCK_DATA]

    def fetch_pokemon_info(self, id: int) -> PokemonInfo:
        for pokemon in self.MOCK_DATA:
            if pokemon.id == id:
                return pokemon
