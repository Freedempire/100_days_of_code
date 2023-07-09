total = float(input('The total: '))
tip = float(input('Percentage of tip: '))
number_of_people = int(input('Number of people: '))
share = total * (1 + tip / 100) / number_of_people
print(f'Each person will need to pay: {share:.2f}')