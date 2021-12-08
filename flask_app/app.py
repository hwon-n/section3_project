from flask import Flask, config




app = Flask(__name__)

@app.route('/')
def index():
    rawg = rawgpy.RAWG(KEY)
    results = rawg.search("Warframe")
    
    return results, 200

if __name__ == "__main__":
    app.run(debug=True)
