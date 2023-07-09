import random

def get_nonempty_string(message, limit):
    while True:
        try:
            nonempty_string = input(message).lower()
            if nonempty_string not in limit:
                raise ValueError
            else:
                return nonempty_string
        except:
            print(f'The input should be one of the following: {", ".join(limit)}.')
        
def get_integer(message, limit):
    while True:
        try:
            integer = int(input(message))
            if limit[0] <= integer <= limit[1]:
                return integer
            else:
                raise ValueError
        except:
            print(f'The number should be between {limit[0]} and {limit[1]}.')

DIFFICULTIES_TIMES = {'easy': 10, 'hard': 5}
NUMBER_RANGE = (1, 100)

print('Welcome to the Number Guessing Game!')
print(f'I\'m thinking of a number between {NUMBER_RANGE[0]} and {NUMBER_RANGE[1]}...')
number = random.randint(*NUMBER_RANGE)
string_limit = list(DIFFICULTIES_TIMES.keys())
difficulty = get_nonempty_string(f"Choose a difficulty. Type {' or '.join(string_limit)}: ", string_limit)
attempts = DIFFICULTIES_TIMES[difficulty]
while attempts > 0:
    print(f'You have {attempts} attempts remaining to guess the number.')
    guess = get_integer('Make a guess: ', NUMBER_RANGE)
    attempts -= 1
    if guess > number:
        print('Too high.\nGuess again.')
    elif guess < number:
        print('Too low.\nGuess again.')
    else:
        break
if guess != number:
    print('You\'ve run out of guesss, you lose.')
else:
    print(f'You got it! The answer was {number}.')
