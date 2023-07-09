def add_together(*num):
    print(type(num)) # num is actually a tuple
    sum = 0
    for n in num:
        sum += n
    return sum

def dict_generator(**kwargs):
    print(type(kwargs)) # kwargs is actually a dictionary
    return kwargs

print(add_together(1, 2, 3))
print(dict_generator(a=1, b=2, c=3))