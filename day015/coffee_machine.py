import sys

DIRECTIONS = ['espresso', 'latte', 'cappuccino', 'report', 'refill', 'off']
COFFEES = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
            'milk': 0
        },
        'price': 1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'coffee': 24,
            'milk': 150
        },
        'price': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100
        },
        'price': 3
    }
}
COIN_VALUES = {
    'pennies': 0.01,
    'nickels': 0.05,
    'dimes': 0.1,
    'quarters': 0.25
}
FULL_RESOURCES = {'water': 300, 'milk': 200, 'coffee': 100}

def get_user_direction():
    while True:
        try:
            direction = input('What would you like? (espresso/latte/cappuccino): ')
            if direction not in DIRECTIONS:
                raise ValueError
            return direction
        except:
            print('Invalid direction.')

def print_report(resources):
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')

def refill(resources):
    for resource in FULL_RESOURCES:
        resources[resource] = FULL_RESOURCES[resource]
    print('The coffee machine is fully refilled.')

def get_int(message, limit, name):
    while True:
        try:
            integer = int(input(message))
            if limit[0] <= integer <= limit[1]:
                return integer
            else:
                raise ValueError
        except:
            print(f'Input an integer for the number of {name}.')

def check_resources_shortage(resources, coffee):
    for ingredient, quantity in COFFEES[coffee]['ingredients'].items():
        if resources[ingredient] < quantity:
            return ingredient

def get_payment():
    print('Please insert coins.')
    quarters = get_int('How many quarters: ', (0, 100), 'quarters')
    dimes = get_int('How many dimes: ', (0, 100), 'dimes')
    nickels = get_int('How many nickels: ', (0, 100), 'nickels')
    pennies = get_int('How many pennies: ', (0, 100), 'pennies')
    return {'quarters': quarters, 'dimes': dimes, 'nickels': nickels, 'pennies': pennies}

def check_payment(payment, coffee):
    # Use round() to remove unnecessary decimal places due to conversion from decimal to binary
    payment_amount = round(sum(value * COIN_VALUES[coin] for (coin, value) in payment.items()), 2)
    change = round(payment_amount - COFFEES[coffee]['price'], 2)
    return payment_amount, change

def make_coffee(resources, coffee):
    for ingredient, quantity in COFFEES[coffee]['ingredients'].items():
        resources[ingredient] -= quantity
    
# Use dictionary's update method to add a new dictionary to the original one,
# or use ** operator or just assign a value to a new key.
# Use dictionary's copy method to make a copy of the original dictionary,
# or use dict(original_dict).
resources = {**FULL_RESOURCES, 'money': 0}

while True:
    direction = get_user_direction()
    if direction == 'report':
        print_report(resources)
    elif direction == 'off':
        print('Turning off...')
        sys.exit()
    elif direction == 'refill':
        refill(resources)
    else:
        shortage = check_resources_shortage(resources, direction)
        if shortage:
            print(f'Sorry there is not enough {shortage}.')
        else:
            payment = get_payment()
            payment_amount, change = check_payment(payment, direction)
            print(f'You have paid {payment_amount}.', end='')
            if change >= 0:
                resources['money'] += COFFEES[direction]['price']
                if change > 0:
                    print(f' Here is ${change} in change.')
                else:
                    print(' Just the right amount of money, no change needed.')
                make_coffee(resources, direction)
                print(f'Here is your {direction} ☕. Enjoy!')
            else:
                print('\nSorry that\'s not enough money. Money refunded.')
