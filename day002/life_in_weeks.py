LIFE_EXPECTATION_YEARS = 90

age = int(input("What is your current age? "))

days = (LIFE_EXPECTATION_YEARS - age) * 365
weeks = (LIFE_EXPECTATION_YEARS - age) * 365 // 7
months = (LIFE_EXPECTATION_YEARS - age) * 12
print(f'You have {days} days, {weeks} weeks, and {months} months left.')