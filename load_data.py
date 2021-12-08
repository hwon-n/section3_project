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



for i in range(1, 251):
    # api를 통해서 데이터 불러오기
    raw_data = requests.get(f'{BASE_URL}{API_KEY}&page={i}')
    parsed_data = json.loads(raw_data.text)
    datas = parsed_data['results']
    
    # MongoDB에 데이터 넣기
    client = MongoClient(MONGO_URI)
    insert = client[DATABASE_NAME][COLLECTION_NAME].insert_many(datas)
        
print('finish insert data!')





