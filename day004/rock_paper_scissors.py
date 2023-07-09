import random

choices = ['rock', 'paper', 'scissors']

user_input = int(input('Your choice? 0 for rock, 1 for paper, 2 for scissors: '))
computer_choice = random.randint(0, 2)

compare = user_input - computer_choice

if compare == 0:
    result = 'Tie'
elif compare == 1 or compare == -2:
    result = 'User wins.'
else:
    result = 'Computer wins.'

print(f'User input: {choices[user_input]}')
print(f'Computer choice: {choices[computer_choice]}')
print(f'Result: {result}')