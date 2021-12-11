import os
import csv
import sqlite3
from flask_app.private import MONGO_PW
from pymongo import MongoClient


# MongoDB 연결 준비
HOST = 'cluster0.qlmif.mongodb.net'
USER = 'hyewon'
PASSWORD = MONGO_PW
DATABASE_NAME = 'Game'
COLLECTION_NAME = 'games'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"



#csv 파일 불러오기
CSV_FILENAME = 'Games.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)

with open(CSV_FILEPATH, 'r') as csv_file:
    dict = csv.DictReader(csv_file)
    
    #MongoDB에 데이터 삽입
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME][COLLECTION_NAME].insert_many(dict)
    