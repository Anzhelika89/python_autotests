import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '01336d14dfc2faf71a23336f05b5c7fe'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
body_post_pokemons = {
    "name": "Груттик",
    "photo_id": 1
}

body_put_pokemons = {
    "pokemon_id": "188044",
    "name": "Кошик",
    "photo_id": 2
}

body_pokemons_pokeball = {
    "pokemon_id": "188044"
}

'''response = requests.post(url = f'{URL}/pokemons',  headers = HEADER, json = body_post_pokemons)
print(response.text)'''

'''response_put = requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_put_pokemons )
print(response_put.text)'''

'''response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokemons_pokeball)
print(response_pokeball.text)'''