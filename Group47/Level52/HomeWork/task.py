
# task 1

print("-------------TASK-1-------------")

def multi_table(number):
    res = ''
    for i in range(1, 11):
        res += f'{i} * {number} = {i*number}\n'
    return res[:-1]

print(multi_table(3))

# task 2

print("-------------TASK-2-------------")

def print_array(arr):
    return ','.join([str(i) for i in arr])

print(print_array([2.0,4.2,5.1,2.2]))

# task 3

print("-------------TASK-3-------------")

def string_clean(s):
    return ''.join([i for i in s if not i.isdigit()])

print_array(string_clean("123456789"))

# task 4

print("-------------TASK-4-------------")

def remove_consecutive_duplicates(s : str) -> str:
    last = ""
    res = []
    for i in s.split():
        if i != last:
            last = i
            res.append(i)
    return ' '.join(res)

print(remove_consecutive_duplicates("aa a aa a aa"))

# task 5

print("-------------TASK-5-------------")

def between_extremes(numbers):
    return max(numbers) - min(numbers)

print(between_extremes([21, 34, 54, 43, 26, 12]))