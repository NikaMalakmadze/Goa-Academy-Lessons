
#task 1

print("-------------TASK-1-------------")

def filter_list(l):
    return [i for i in l if type(i) == int]

print(filter_list([1, 2, 'a', 'b']))

#task 2

print("-------------TASK-2-------------")

def square_digits(num):
    return int(''.join([str(int(i)**2) for i in str(num)]))

print(square_digits(9119))

#task 3

print("-------------TASK-3-------------")

def get_middle(s):
    return s[(len(s)//2)-1: (len(s)//2)+1] if len(s)%2 == 0 else s[len(s)//2] 

print(get_middle('test'))

#task 4

print("-------------TASK-4-------------")

def find_short(s):
    return min([len(l) for l in s.split()])

print(find_short("lets talk about javascript the best language"))

#task 5

print("-------------TASK-5-------------")

def solution(text, ending):
    return text.endswith(ending)

print(solution("samurai", "ra"))