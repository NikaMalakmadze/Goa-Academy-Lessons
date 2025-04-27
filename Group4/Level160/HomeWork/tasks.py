
# task 1

import math

def branch(n):
    if n == 1: return 0
    element_layer = math.ceil((math.sqrt(n)+1)/2)
    branch_start = ((element_layer-1)*2 - 1)**2+1
    side_len = (element_layer-1)*2
    branch_nomer = 0
    i = 1
    while branch_start != n:
        if i%side_len == 0: branch_nomer += 1
        branch_start += 1
        i += 1
    return branch_nomer

print(branch(50))

# task 2

def to_binary(n):
    res = ''
    while n != 0:
        res += f'{n % 2}'
        n = n // 2
    return int(res[::-1])

print(to_binary(5))

# task 3

def josephus_survivor(n,k):
    arr = list(range(1, n+1))
    delete_index = 0
    while len(arr) != 1:
        delete_index += k - 1 
        if delete_index > len(arr) - 1:
            delete_index = delete_index % len(arr)
        arr.pop(delete_index)
    return arr[0]

print(josephus_survivor(100,1))

# task 4

def move_zeros(lst):
    count = lst.count(0)
    while 0 in lst:
        lst.remove(0)
    return lst + [0]*count

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))

# task 5

from itertools import zip_longest

def sum_strings(x, y):
    res = []
    num_x = list(x)
    num_y = list(y)
    additional = 0
    
    for digit_x, digit_y in zip_longest(num_x[::-1], num_y[::-1], fillvalue='0'):
        digits_sum = int(digit_x)+int(digit_y) + additional
        additional, digit = digits_sum // 10, digits_sum % 10
        res.append(str(digit))
    
    if additional:
        res.append(str(additional))
    return ''.join(res[::-1]).lstrip('0') or '0'

print(sum_strings("123", "456"))