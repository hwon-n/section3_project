from flask import Flask, render_template, request




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html'), 200
    elif request.method == 'POST':
        result = request.form
        return render_template('index.html', result=result), 200


if __name__ == "__main__":
    app.run(debug=True)


