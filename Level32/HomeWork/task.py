
#task 1

print("-------------TASK-1-------------")

def string_to_array(s):
    return s.split(' ')

print(string_to_array('just String'))

#task 2

print("-------------TASK-2-------------")

def string_to_number(s):
    return int(s)

print(string_to_number('533'))

#task 3

print("-------------TASK-3-------------")

def fake_bin(x):
    return ''.join(["0" if i < "5" else "1" for i in x])

print(fake_bin("45385593107843568"))

#task 4

print("-------------TASK-4-------------")

def high_and_low(n):
    return f"{max(map(int, n.split()))} {min(map(int, n.split()))}"

print(high_and_low("1 2 3 -5"))