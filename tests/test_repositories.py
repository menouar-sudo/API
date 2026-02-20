from pokedex.repositories import APIPokemonRepository, MockPokemonRepository


class TestFetchPokemonsFromAPI:
    def test_fetch_all_pokemons(self):
        repository = APIPokemonRepository()

        pokemons = repository.fetch_all_pokemons()

        assert pokemons

    def test_fetch_pokemon_using_id(self):
        repository = APIPokemonRepository()

        pokemon = repository.fetch_pokemon_info("1")

        assert pokemon["name"] == "bulbasaur"


class TestFetchPokemonsFromMock:
    def test_fetch_all_pokemons(self):
        repository = MockPokemonRepository()

        pokemons = repository.fetch_all_pokemons()

        assert pokemons

    def test_fetch_pokemon_using_id(self):
        repository = MockPokemonRepository()

        pokemon = repository.fetch_pokemon_info("1")

        assert pokemon["name"] == "toufik"
