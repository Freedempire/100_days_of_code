import random
import os

from hlg_data import data

LOGO = """
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗                
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗               
███████║██║██║  ███╗███████║█████╗  ██████╔╝               
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗               
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║               
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝               
                                                           
                ██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
                ██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
                ██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
                ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
                ███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
                ╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
"""

VS = """
██    ██ ███████    
██    ██ ██         
██    ██ ███████    
 ██  ██       ██    
  ████   ███████ ██ 
"""

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def get_parts():
    while True:
        sample = random.sample(data, 2)
        if sample[0]['follower_count'] != sample[1]['follower_count']:
            return sample

def show_part(order, part):
    if order == 'A':
        print(f'Compare {order}: ', end='')
    else:
        print(f'Against {order}: ', end='')
    print(f'{part["name"]}, {part["description"]}, from {part["country"]}')

def get_guess():
    while True:
        try:
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if guess not in ('a', 'b'):
                raise ValueError
            else:
                return guess
        except:
            print("You answer can only be 'A' or 'B'.")

def check_guess(parts, guess):
    if parts[0]['follower_count'] > parts[1]['follower_count']:
        answer = 'a'
    else:
        answer = 'b'
    return guess == answer
    
score = 0
while True:
    parts = get_parts()
    print(LOGO)
    show_part('A', parts[0])
    print(VS)
    show_part('B', parts[1])
    guess = get_guess()
    clear()
    if check_guess(parts, guess):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break