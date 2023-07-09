import random
import os
import time
import string

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def word_spelling(word, guessed=''):
    spelling = []
    for l in word:
        if l in guessed:
            spelling.append(l)
        else:
            spelling.append('_')
    return ' '.join(spelling)

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra').split()

OPPOTUNITIES_TOTAL = 6
oppotunities_left = OPPOTUNITIES_TOTAL
won = False
letters_tried = ''
letters_right = ''
word = random.choice(words)
spelling = word_spelling(word)

while oppotunities_left and not won:
    clear()
    print(HANGMANPICS[OPPOTUNITIES_TOTAL - oppotunities_left])
    print(spelling)
    try:
        guess = input('Your guess of the letter: ')[0].lower()
        if guess not in string.ascii_lowercase:
            raise ValueError
    except KeyboardInterrupt:
        print('\nTerminated by user. Bye.')
        exit()
    except:
        print('Invalid guess, try again.')
        time.sleep(0.8)
        continue
    if guess in letters_tried:
        print('You already guessed the letter.')
        # print('\a')
        time.sleep(0.8)
        continue
    letters_tried += guess
    if guess in word:
        letters_right += guess
        spelling = word_spelling(word, letters_right)
        if '_' not in spelling:
            won = True
    else:
        oppotunities_left -= 1

clear()
print(HANGMANPICS[OPPOTUNITIES_TOTAL - oppotunities_left])
print(spelling)

result = 'won' if won else 'lost'

print(f'You {result}! The word is {word}.')