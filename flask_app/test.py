import requests
import json
from private import API_KEY, MONGO_PW
from pymongo import MongoClient

HOST = 'cluster0.qlmif.mongodb.net'
USER = 'hyewon'
PASSWORD = MONGO_PW
DATABASE_NAME = 'Test'
COLLECTION_NAME = 'testdb'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

data = {
    1: {'id': 1,
     'test': 3},
    2: {'id': 2,
     'test': 2},
    3: {
        'id':3,
        'test':4
    }
}

client = MongoClient(MONGO_URI)
collection = client[DATABASE_NAME]
db = collection[COLLECTION_NAME].insert_many(data)

print('finish insert data!')