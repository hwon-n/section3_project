import requests
import json
from private import API_KEY, MONGO_PW
import sqlite3
import os
from random import randint


BASE_URL = 'https://api.rawg.io/api/games?key='

DB_FILENAME = 'Game.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

raw_data = requests.get(f'{BASE_URL}{API_KEY}&page=1')
parsed_data = json.loads(raw_data.text)
datas = parsed_data['results']

random = randint(1, len(datas[10]['parent_platforms']))
added = datas[10]['added']
playtime = datas[10]['playtime']
platform = datas[10]['parent_platforms'][random]['platform']['name']
genre_1 = datas[10]['genres'][0]['name']
try:
    genre_2 = datas[10]['genres'][1]['name']
except IndexError:
    genre_2 = 'Only one genre'
tag_1 = datas[10]['tags'][0]['name']
tag_2 = datas[10]['tags'][1]['name']
try:
    esrb_rating = datas[10]['esrb_rating']['name']
except TypeError:
    esrb_rating = 'No age info'


# 테이블 생성

create_table = """
CREATE TABLE Game_info(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Added INTEGER,
    Playtime INTERGER,
    Platform VARCHAR(30),
    Genre_1 VARCHAR(20),
    Genre_2 VARCHAR(20),
    Tag_1 VARCHAR(20),
    Tag_2 VARCHAR(20),
    Esrb_rating VARCHAR(30)
);
"""

print(platform)