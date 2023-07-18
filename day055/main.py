from flask import Flask
from markupsafe import escape


def make_bold(func):
    def wrapper():
        print(2)
        return f'<b>{func()}</b>'
    return wrapper

def make_emphasis(func):
    def wrapper():
        return f'<em>{func()}</em>'
    return wrapper

def make_underlined(func):
    def wrapper():
        print(1)
        return f'<u>{func()}</u>'
    return wrapper

app = Flask(__name__)

@app.route('/')
@make_bold
@make_underlined
def index():
    return 'index'

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/greet/<name>')
def greet(name):
    return f'hello {escape(name)}'


# flask --app main run --debug
if __name__ == '__main__':
    app.run(debug=True)

