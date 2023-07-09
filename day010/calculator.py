CALCULATOR_ASCII = """
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

first_operand = None
second_operand = None
operator = None
result = None
choice = None

print(CALCULATOR_ASCII)

while True:
    if choice is None or choice != 'y':
        print('=' * 80)
        first_operand = float(input('What is the first operand: '))
    operator = input('Pick up an operator (' + ', '.join(operations.keys()) + '): ')
    second_operand = float(input('What is the second operand: '))

    # if operator == '+':
    #     result = add(first_operand, second_operand)
    # elif operator == '-':
    #     result = subtract(first_operand, second_operand)
    # elif operator == '*':
    #     result = multiply(first_operand, second_operand)
    # else:
    #     result = divide(first_operand, second_operand)

    result = operations[operator](first_operand, second_operand)

    print(f'{first_operand} {operator} {second_operand} = {result:.2f}')
    choice = input((f'Type \'y\' to continue calculating with {result:.2f}, or type \'n\' to '
                    'start a new calculation: '))
    if choice == 'y':
        first_operand = result
