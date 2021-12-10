from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

FILENAME = 'model.pkl'
MODEL_PATH = os.path.join(os.pardir, FILENAME)


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html'), 200
    elif request.method == 'POST':
        Playtime = request.form.get('Playtime', type=int)
        Platform = request.form.get('Platform', type=int)
        Genres = request.form.get('Genres')
        Stores = request.form.get('Stores', type=int)
        Tag = request.form.get('Tag')
        Esrb_rating = request.form.get('Esrb_rating')
        
        model = None
        with open(MODEL_PATH, 'rb') as pickle_file:
            model = pickle.load(pickle_file)
        
        X_test = pd.DataFrame({
            "Playtime": [Playtime], 
            "Platform": [Platform],
            "Genres":[Genres],
            "Stores": [Stores],
            "Tag": [Tag],
            "Esrb_rating": [Esrb_rating]
        })
        
        y_pred = int(model.predict(X_test))
        
        return render_template('index.html', result=y_pred), 200
        
        
    


if __name__ == "__main__":
    app.run(debug=True)


