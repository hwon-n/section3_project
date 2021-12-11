from flask import Flask, render_template, request
from private import MONGO_PW
from pymongo import MongoClient
import pandas as pd
import pickle
import os


FILENAME = 'model.pkl'
MODEL_PATH = os.path.join(os.pardir, FILENAME)


# MongoDB 연결 준비
HOST = 'cluster0.qlmif.mongodb.net'
USER = 'hyewon'
PASSWORD = MONGO_PW
DATABASE_NAME = 'Game'
COLLECTION_NAME = 'apiResult'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html'), 200
    
    # html에서 submit 버튼 눌렀을 때
    elif request.method == 'POST':
        model = None
        with open(MODEL_PATH, 'rb') as pickle_file:
            model = pickle.load(pickle_file)
        
        # 예측하기 위해 값 DataFrame으로 저장
        X_test = pd.DataFrame({
            "Playtime": [request.form.get('Playtime', type=int)], 
            "Platform": [request.form.get('Platform', type=int)],
            "Genres":[request.form.get('Genres')],
            "Stores": [request.form.get('Stores', type=int)],
            "Tag": [request.form.get('Tag')],
            "Esrb_rating": [request.form.get('Esrb_rating')]
        })
        
        y_pred = int(model.predict(X_test))
        
        # 예측 결과 포함해 MongoDB에 저장
        X_test['Added'] = y_pred
        dict = X_test.loc[0].to_dict()
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME][COLLECTION_NAME].insert_one(dict)
        
        return render_template('index.html', result=y_pred), 200
        
        
    

if __name__ == "__main__":
    app.run(debug=True)


