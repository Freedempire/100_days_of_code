from flask import Flask
from random import randint

app = Flask(__name__)

winner_number = randint(0, 9)


def checker_decorator(fn):
    def wrap(number):
        if int(number) == winner_number:
            return fn(number)
        elif int(number) < winner_number:
            return '<h1>Too low!</h1>' \
                   '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" height="200">'
        else:
            return '<h1>Too high!</h1>' \
                   '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" height="200">'

    return wrap


@app.route('/')
def greetings():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" height="200">'


@app.route('/<number>')
@checker_decorator
def congratulations(number):
    return f'<h1>Correct! The chosen number was:{number}</h1>' \
           f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" height="200">'


if __name__ == "__main__":
    app.run(debug=True)