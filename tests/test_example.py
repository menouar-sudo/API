import requests
import random


def my_function():
    url = "https://pokeapi.co/api/v2/pokemona/"

    r = requests.get(url)
    data = r.json()

    print("Welcome to the Game\nWhoOoOoO's That Pokemon")
    choice = random.randint(1, len(data["results"]))

    return choice


def test_choice():
    choice = my_function()

    assert choice is not None


def test_multiply():
    assert 1 * 2 == 3, "result should be 2"
