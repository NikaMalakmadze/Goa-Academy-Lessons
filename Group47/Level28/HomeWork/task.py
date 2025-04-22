
#task 1

print("-------------TASK-1-------------")

def bool_to_word(boolean):
    return "Yes" if boolean else 'No'

print(bool_to_word(True))

#task 2

print("-------------TASK-2-------------")

def remove_char(s):
    return s[1:-1]

print(remove_char("1Nika1"))

#task 3

print("-------------TASK-3-------------")

def string_to_number(s):
    return int(s)

print(string_to_number("123"))

#task 4

print("-------------TASK-4-------------")

def no_space(x):
    return x.replace(' ', '')

print(no_space('8aaaaa dddd r     '))

#task 5

print("-------------TASK-5-------------")

def sum_array(a):
    return sum(a) if a else 0

print(sum_array([1, 2, 3]))