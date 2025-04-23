
# task 1

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

print(min_length_num(8, 16))