import random

from flask import Flask
# from markupsafe import escape


app = Flask(__name__)


def high_low_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            return '<h1 style="color: green">You found me!</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="200px">'
        elif result < 0:
            return '<h1 style="color: red">Too low, try again!</h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="200px">'
        else:
            return '<h1 style="color: purple">Too high, try again!</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="200px">'
    return wrapper


@app.route('/')
def guess():
    return '<h1>Guess a number between 0 and 9</h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="200px">'


@app.route('/<int:num>') # num will be passed as keyword argument
@high_low_decorator
def judge(num):
    return num - random_number


random_number = random.randint(0, 9)

app.run(debug=True)