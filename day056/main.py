from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return 'Hello world!'
    return render_template('index.html')

@app.route('/personal')
def personal():
    return render_template('personal.html')

# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello():
#     return 




app.run(debug=True)