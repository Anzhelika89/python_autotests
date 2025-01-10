import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '01336d14dfc2faf71a23336f05b5c7fe'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '14456'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID })
    assert response.status_code == 200

def test_name_trainers():
    response_get = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID })
    assert response_get.json()["data"] [0] ["trainer_name"] == 'Мудрый Дрон'

    