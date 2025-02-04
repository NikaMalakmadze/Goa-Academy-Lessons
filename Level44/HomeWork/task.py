
# task 1

print("-------------TASK-1-------------")

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin("1"))

# task 2

print("-------------TASK-2-------------")

def row_sum_odd_numbers(n):
    return sum(i for i in range(n*(n-1)+1,n*(n-1)+1 + (n*2), 2))

print(row_sum_odd_numbers(3))

# task 3

print("-------------TASK-3-------------")

def binary_array_to_number(arr):
    return int(''.join(str(i) for i in arr), 2)

print(binary_array_to_number([1,1,1,1]))

# task 4

print("-------------TASK-4-------------")

def min_max(lst):
    return [min(lst), max(lst)]

print(min_max([1,2,3,4,5]))

# task 5

print("-------------TASK-5-------------")

def divisors(integer):
    divisors = [i for i in range(2, integer//2 + 1) if integer%i == 0]
    return f'{integer} is prime' if not divisors else divisors

print(divisors(34))