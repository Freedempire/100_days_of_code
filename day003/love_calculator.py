print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true_times = {'t': 0, 'r': 0, 'u': 0, 'e': 0}
love_times = {'l': 0, 'o': 0, 'v': 0, 'e': 0}

name = (name1 + name2).lower().replace(' ', '')

# count() of string is also useful here
for c in 'true':
    for l in name:
        if l == c:
            true_times[c] += 1

for c in 'love':
    for l in name:
        if l == c:
            love_times[c] += 1

true_total = sum(true_times.values())
love_total = sum(love_times.values())

score = true_total * 10 + love_total

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')