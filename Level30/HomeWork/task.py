
#task 1

print("-------------TASK-1-------------")

def positive_sum(arr):
    return sum([i for i in arr if i > 0])

print(positive_sum([-1,2,3,4,-5]))

#task 2

print("-------------TASK-2-------------")

def square_sum(numbers):
    return sum([i*i for i in numbers])

print(square_sum([0, 3, 4, 5]))

#task 3

print("-------------TASK-3-------------")

def sum_array(a):
    return sum(a)

print(sum_array([1, 5.2, 4, 0, -1]))

#task 4

print("-------------TASK-4-------------")

def find_average(a):
    return sum(a) / len(a) if a else 0

print(find_average([1, 2, 3]))

#task 5

print("-------------TASK-5-------------")

def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if arr else []

print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))