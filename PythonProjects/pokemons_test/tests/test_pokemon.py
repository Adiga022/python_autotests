import requests
import pytest

token = '56bbd4e35c994b531769066a45835267'
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': f'{token}'
}
def test_get_trainers():

    response = requests.get(url=f'{URL}/trainers', headers=HEADER)
    assert response.status_code == 200, f'Неверный код'

def test_get_trainers_name():

    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3554}, headers=HEADER)
    assert response.json()['trainer_name'] == 'God Of War', f'Имя не принадлежит пользователю'
