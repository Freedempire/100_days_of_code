import random
import string

LETTERS = string.ascii_letters
SYMBOLS = string.punctuation
DIGITS = string.digits

number_of_letters = int(input('Number of letters: '))
number_of_symbols = int(input('Number of symbols: '))
number_of_digits = int(input('Number of digits: '))

password = ''

for l in range(0, number_of_letters):
    password += random.choice(LETTERS)

for s in range(0, number_of_symbols):
    password += random.choice(SYMBOLS)

for d in range(0, number_of_digits):
    password += random.choice(DIGITS)

password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)
print(password)