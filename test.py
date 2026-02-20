from pokemon.repositories import APIPokemonRepository


class TestAPIPokemonRepository:
    def test_fetch_all_pokemons(self):

        repository = APIPokemonRepository()

        pokemons = repository.fetch_all_pokemons()
