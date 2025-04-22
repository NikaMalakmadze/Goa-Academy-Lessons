
# task 1

print("-------------TASK-1-------------")

def vowel_one(s):
    return ''.join('1' if i in 'aeiouAEIOU' else '0' for i in s)

print(vowel_one('Codewars'))

# task 2

print("-------------TASK-2-------------")

from math import gcd
def reduce_fraction(fraction):
    n = gcd(*fraction)
    return tuple(map(lambda x: x/n, fraction))

print(reduce_fraction((80, 120)))

# task 3

print("-------------TASK-3-------------")

import string
def count_letters_and_digits(s):
    ld = string.ascii_letters + string.digits
    return sum(1 for i in s if i in ld)

print(count_letters_and_digits('u_n_d_e_r__S_C_O_R_E'))

# task 4

print("-------------TASK-4-------------")

def solution(text, ending):
    return text.endswith(ending)

print(solution("samurai", "ai"))

# task 5

print("-------------TASK-5-------------")

def elimination(arr):
    for i in arr:
        if arr.count(i) == 2:
            return i

print(elimination([3, 3]))