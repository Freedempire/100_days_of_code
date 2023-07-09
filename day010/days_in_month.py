DAYS_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False

def days_in_month(year, month):
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return DAYS_IN_MONTHS[month - 1]

# print(is_leap_year(int(input('Year: '))))

print(days_in_month(int(input('Year: ')), int(input('Month: '))))