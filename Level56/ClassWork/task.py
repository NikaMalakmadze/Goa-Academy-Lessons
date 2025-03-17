
# task 1

def drink(amount, limit):
    return 'limit reached' if amount > limit else 'Ok'

print(drink(34, 60))

# task 2

def is_yuri(n, m):
    return True if n == 120 and m == 80 else False

print(is_yuri(34, 43))

# task 3

def captain(ship_cost, coins):
    return 'ok' if ship_cost in list(range(150, 351, 50)) and coins >= ship_cost else 'You are not captain'

print(captain(350, 351))

# task 4

def apples(arr):
    return list(set(arr))

print(apples(['saxeoba1','saxeoba1','saxeoba13','saxeoba2','saxeoba3','saxeoba2','saxeoba5','saxeoba13']))

# task 5

def solve(s):
    l = 0
    u = 0
    for i in s:
        if i.isupper(): 
            u += 1
        else:
            l += 1
    return s.lower() if l>=u else s.upper()

print(solve("code"))