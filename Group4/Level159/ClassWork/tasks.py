
# task 1

def sum_triangular_numbers(n):
    a = 0
    res = 0
    for i in range(n):
        a += i + 1
        res += a
    return res

print(sum_triangular_numbers(3))