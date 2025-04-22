
# task 1

print("-------------TASK-1-------------")

def simple_multiplication(n) :
    return n*8 if n%2 == 0 else n*9

print(simple_multiplication(34))

# task 2

print("-------------TASK-2-------------")

def invert(lst):
    return [-i for i in lst]

print(invert([1,2,3,4,5]))

# task 3

print("-------------TASK-3-------------")

def fake_bin(x):
    return ''.join("0" if i < "5" else "1" for i in x)

print(fake_bin("509321967506747"))

# task 4

print("-------------TASK-4-------------")

def string_to_array(s):
    return s.split(" ")

print(string_to_array("I love arrays they are my favorite"))

# task 5

print("-------------TASK-5-------------")

def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == 'rock':
        return "Player 1 won!"
    elif p1 == 'rock' and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == p2:
        return "Draw!"
    return "Player 2 won!"

print(rps('scissors', 'rock'))

# task 6

print("-------------TASK-6-------------")

def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'

print(greet('Daniel', 'Daniel'))

# task 7

print("-------------TASK-7-------------")

def monkey_count(n):
    return [i for i in range(1, n+1)]

print(monkey_count([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# task 8

print("-------------TASK-8-------------")

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [human_years,15, 15 ]
    if human_years == 2:
        return [human_years, 24, 24]
    else:
        return [human_years, 24 + ((human_years - 2) * 4), 24 + ((human_years - 2) * 5)]
    
print(human_years_cat_years_dog_years(10))

# task 9

print("-------------TASK-9-------------")

def is_isogram(string):
    return len(string) == len(set(string.lower()))

print(is_isogram("Dermatoglyphics"))

# task 10

print("-------------TASK-10-------------")

def binary_array_to_number(arr):
    return int(''.join(str(i) for i in arr), 2)

print(binary_array_to_number([1,1,1,1]))