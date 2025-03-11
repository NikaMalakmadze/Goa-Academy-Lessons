
# task 1

print("-------------TASK-1-------------")

def sort_by_length(arr):
    return sorted(arr, key=lambda x: len(x))

print(sort_by_length(["short", "longer", "longest"]))

# task 2

print("-------------TASK-2-------------")

def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))

print(sequence_sum(16, 15, 3))

# task 3

print("-------------TASK-3-------------")

def series_sum(n):
    sum = 0
    count = 0
    index = 1
    while count < n:
        sum += 1/index
        index += 3
        count += 1
    return f'{sum:.2f}'

print(series_sum(3))

# task 4

print("-------------TASK-4-------------")

def round_to_next5(n):
    x = n % 5
    return n if x==0 else n+(5-x)

print(round_to_next5(42))

# task 5

print("-------------TASK-5-------------")

def two_oldest_ages(ages):
    return sorted(ages)[-2:]

print(two_oldest_ages([6, 5, 83, 5, 3, 18]))