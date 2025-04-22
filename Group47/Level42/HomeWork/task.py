
# task 1

print("-------------TASK-1-------------")

def sum_mix(arr):
    return sum([int(i) for i in arr])

print(sum_mix([9, 3, '7', '3']))

# task 2

print("-------------TASK-2-------------")

def double_char(s):
    return ''.join(i*2 for i in s)

print(double_char("Hello World"))

# task 3

print("-------------TASK-3-------------")

def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

print(sum_mix([100, 200, 300], [400, 500, 600]))

# task 4

print("-------------TASK-4-------------")

def reverse_words(s):
    return ' '.join(i for i in s.split()[::-1])

print(reverse_words("hello world!"))

# task 5

print("-------------TASK-5-------------")

def sum_str(a, b):
    if a and b:
        return str(int(a)+int(b))
    elif a and not b:
        return a
    elif not a and b:
        return b
    else:
        return '0'
    
print(sum_str("34","5"))