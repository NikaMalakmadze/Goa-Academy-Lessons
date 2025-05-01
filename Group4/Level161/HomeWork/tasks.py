
# Sum Strings as Numbers
#   Solved using numpy

import numpy as np
def sum_strings(x, y):
    num_x = [int(i) for i in x]
    num_y = [int(i) for i in y]
    len_x = len(num_x)
    len_y = len(num_y)

    if len_x > len_y:
        num_y = [0] * (len_x - len_y) + num_y
    elif len_y > len_x:
        num_x = [0] * (len_y - len_x) + num_x
            
    sum_arr = list(np.array(num_x) + np.array(num_y))
    for i in range(len(sum_arr)-1, -1, -1):
        if sum_arr[i] >= 10:
            sum_arr[i] = sum_arr[i] % 10
            if i > 0:
                sum_arr[i-1] += 1
            else:
                sum_arr.insert(0, 1)
                
    return ''.join(str(i) for i in sum_arr).lstrip('0') or '0'

print(sum_strings("123", "456"))

# Progressive Spiral Number Branch
#   Solved with different solution

import math
def branch(n):
    if n == 1: return 0
    element_layer = math.ceil((math.sqrt(n)+1)/2)
    branch_start = ((element_layer-1)*2 - 1)**2+1
    return (n - branch_start) // ((element_layer-1)*2)

print(branch(50))