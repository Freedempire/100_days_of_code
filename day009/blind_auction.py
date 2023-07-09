import os

clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

print('Welcome to the secret auction program.')

bid_record = []

while True:
    name = input('What is your name: ')
    bid = input('What is your bid: ')
    bid_record.append(dict(name=name, bid=bid))
    if input('Are there any other bidders (type \'yes\' or \'no\'): ') == 'no':
        clear_screen()
        break
    clear_screen()

highest_bid_index = 0

for index, record in enumerate(bid_record):
    if record['bid'] > bid_record[highest_bid_index]['bid']:
        highest_bid_index = index

print(f'The winner is {bid_record[highest_bid_index]["name"]} with a bid of '
      f'{bid_record[highest_bid_index]["bid"]}.')

