
# task 1

#V1
# works but need more than 12s

def calc_n(ord_max):
    num = 0
    digit = 1
    for i in range(ord_max-1, 0, -1):
        num += digit**i
        digit += 1
    return num

def min_length_num(num_dig, ord_max, n=1):
    if n > ord_max: return [False, -1]
    num = calc_n(n)
    if len(str(num)) == num_dig: return [True, n]
    return min_length_num(num_dig, ord_max, n+1)

#V2
# works, but still need more than 12s

from math import log10

def min_length_num_V2(num_dig, ord_max):
    for term in range(1, ord_max+1):
        num = sum((i**(term-i)) for i in range(1, term))
        if num > 0:
            digits = int(log10(num)) + 1
            if digits == num_dig: return [True, term]
    return [False, -1]

print(min_length_num_V2(8, 16))

#V3
# Passed all tests, works in less than 4s

from math import log10 

def calc_n(ord_max):
    num = 1
    for i in range(1, ord_max):
        num += pow(i, ord_max-i)
    return int(log10(num)) + 1 

def min_length_num(num_dig, ord_max):
    left = 0
    right = ord_max
    while left <= right:
        middle = (left+right)//2
        middle_n = calc_n(middle)
        if middle_n == num_dig:
            while calc_n(middle) == num_dig:
                middle -= 1
            return [True, middle + 1]
        elif middle_n > num_dig:
            right = middle - 1
        else:
            left = middle + 1
    return [False, -1]

print(min_length_num_V2(8, 16))
