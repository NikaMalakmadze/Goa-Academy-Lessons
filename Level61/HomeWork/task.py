
# task 1

print("-------------TASK-1-------------")

def first_non_consecutive(arr):
    for i in range(arr[0], arr[-1]):
        if i not in arr: return i + 1

print(first_non_consecutive([1,2,3,4,6,7,8]))

# task 2

print("-------------TASK-2-------------")

def to_alternating_case(string):
    return string.swapcase()

print(to_alternating_case("hello world"))

# task 3

print("-------------TASK-3-------------")

def correct(s):
    return s.replace("5", "S").replace("0", "O").replace("1", "I")

print(correct("L0ND0N"))

# task 4

print("-------------TASK-4-------------")

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(correct("L0ND0N"))

# task 5

print("-------------TASK-5-------------")

def final_grade(e, p):
    if e > 90 or  p > 10: return 100
    if e > 75 and p >= 5: return 90
    if e > 50 and p >= 2: return 75
    return 0

print(final_grade(100, 12))

# task 6

print("-------------TASK-6-------------")

def bonus_time(salary, bonus):
   return '$' +str(salary * 10) if bonus else '$'+str(salary)

print(bonus_time(10000, True))

# task 7

print("-------------TASK-7-------------")

def min_max(lst):
    return [min(lst), max(lst)]

print(min_max([1,2,3,4,5]))