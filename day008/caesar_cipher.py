import string

ALPHABET = string.ascii_lowercase

def caesar_cipher(message, shift, direction='e'):
    new_message = ''
    shift = -shift if direction == 'd' else shift
    for c in message:
        if c in ALPHABET:
            new_message += ALPHABET[(ALPHABET.index(c) + shift) % 26]
        else:
            new_message += c
    return new_message


direction = input('Choose direction, e for encode, d for decode: ')
shift = int(input('Shift number: '))
message = input('Message you want to process:\n').lower()


print(caesar_cipher(message, shift, direction))
