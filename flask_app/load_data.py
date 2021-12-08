from private import API_KEY, MONGO_PW
from pymongo import MongoClient
import requests
import json

BASE_URL = 'https://api.rawg.io/api/games?key='

HOST = 'cluster0.qlmif.mongodb.net'
USER = 'hyewon'
PASSWORD = MONGO_PW
DATABASE_NAME = 'Games'
COLLECTION_NAME = 'game_info'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"


added = []

for i in range(1, 10):
    raw_data = requests.get(f'{BASE_URL}{API_KEY}&page={i}')
    parsed_data = json.loads(raw_data.text)
    all_game_data = parsed_data['results']
    for count in range(1, len(all_game_data)):
        added.append(all_game_data[count]['added'])

print(added)