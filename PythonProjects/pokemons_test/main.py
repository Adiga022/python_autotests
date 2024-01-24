"""
Test
"""
import requests

token = '56bbd4e35c994b531769066a45835267'
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': f'{token}'
          }
body_сreate  = {
    "name": "King",
    "photo": "https://dolnikov.ru/pokemons/albums/452.png"
}
# Создаем покемона и присваем id созданного покемона переменной
response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_сreate)
parsed_response = response.json()
pokemon_id = parsed_response['id']
print(f'ID покемона: {pokemon_id}')
print(response.text, f'Статус кода: {response.status_code}')

body_change = {
    "pokemon_id": f"{pokemon_id}",
    "name": "NewName1",
    "photo": "https://dolnikov.ru/pokemons/albums/452.png"
}

#обновляем имя покемона
response = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)
print(response.text, f'Стаутс кода: {response.status_code}')

body_pokeball = {
    "pokemon_id": f"{pokemon_id}"
}
#ловим покемона в покебол
response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(response.text, f'Статус кода: {response.status_code}')



