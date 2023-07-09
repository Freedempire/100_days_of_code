def prime_checker(number):
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0 and number != n:
            print("It's not a prime number.")
            return
    print("It's a prime number.")

number = int(input('Number to check: '))
prime_checker = prime_checker(number)