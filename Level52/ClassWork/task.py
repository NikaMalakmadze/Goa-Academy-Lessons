
# task 1

def find_next_square(sq):
    return (sq**0.5 + 1)**2 if (sq**0.5%1 == 0) else -1

print(find_next_square(54))

# task 2

def min_max(lst):
    return [min(lst), max(lst)]

print(min_max([2334454,5]))

# task 3

def series_sum(n):
    sum = 0
    count = 0
    index = 1
    while count < n:
        sum += 1/index
        index += 3
        count += 1
    return f'{sum:.2f}'

print(series_sum(5))