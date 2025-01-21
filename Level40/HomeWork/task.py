
#task 1

print("-------------TASK-1-------------")

def remove_duplicate_words(s):
    output = []
    [output.append(word) for word in s.split() if word not in output]
    return ' '.join(output)

print(remove_duplicate_words("my cat is my cat fat"))

#task 2

print("-------------TASK-2-------------")

def stray(arr):
    return list(filter(lambda x: arr.count(x) == 1, arr))[0]

print(stray([1, 1, 1, 1, 1, 1, 2]))

#task 3

print("-------------TASK-3-------------")

def solution(nums):
    return [] if not nums else sorted(nums)

print(solution([1,2,3,10,5]))

#task 4

print("-------------TASK-4-------------")

def capitals(word):
    arr = []
    for index, char in enumerate(word):
        if char.isupper():
            arr.append(index)
    return arr

print(capitals('CodEWaRs'))

#task 5

print("-------------TASK-5-------------")

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(factorial(10))