
# task 1

print("-------------TASK-1-------------")

def high_and_low(n):
    return f'{max(map(int, n.split()))} {min(map(int, n.split()))}'

print(high_and_low("1 9 3 4 -5"))

# task 2

print("-------------TASK-2-------------")

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin('4353'))

# task 3

print("-------------TASK-3-------------")

def odd_or_even(arr):
    return 'even' if sum(arr)%2 == 0 else 'odd'

print(odd_or_even([1023, 1, 2]))

# task 4

print("-------------TASK-4-------------")

def solution(nums):
    return [] if not nums else sorted(nums)

print(solution([20,2,10]))

# task 5

print("-------------TASK-5-------------")

def greet(name): 
    return f'Hello {name.capitalize()}!'

print(greet('BILLY'))