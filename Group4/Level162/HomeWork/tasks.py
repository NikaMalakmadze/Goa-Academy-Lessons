
# task 1

def unique_sum(lst):
    return sum(set(lst)) if lst else None

print(unique_sum([1,3,8,1,8]))

# task 2

def add(lst):
    return [sum(lst[:i+1]) for i in range(len(lst))]

print(add([5,10,15,20,25,30,35,40]))

# task 3

def is_prime(n):
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0: return False
    return True

def total(arr):
    return sum(arr[i] for i in range(2, len(arr)) if is_prime(i))

print(total([1,2,3,4,5,6,7,8,9,10,11,12,13]))