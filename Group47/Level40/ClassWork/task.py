
#task 1

def password(st):
    if len(st) >= 8:
        upper = False
        lower = False
        digit = False
        for char in st:
            if char.isupper():
                upper = True
            if char.islower():
                lower = True
            if char.isdigit():
                digit = True
        return upper and lower and digit
    return False

print(password('Fejami34'))

# task 2

def is_isogram(string):
    return len(string) == len(set(string.lower()))

print(is_isogram('aba'))

# task 3

def friend(x):
    return [i for i in x if len(i) == 4]

print(friend(['lorem', 'ipsum', 'rote']))

# task 4

def validate_pin(pin):
    return len(pin) == 4 and pin.isdigit() or len(pin) == 6 and pin.isdigit()

print(validate_pin('342'))