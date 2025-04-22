
#task 1

print("-------------TASK-1-------------")

for i in range(1, 50, 2):
    print("GOA" , i)

#task 2

print("-------------TASK-2-------------")

for i in range(3):
    for j in range(3):
        print("*" , end="")
    print()

#task 3

print("-------------TASK-3-------------")

for i in range(3):
    for j in range(10):
        print("*" , end="")
    print()

#task 4

print("-------------TASK-4-------------")

for num1 in range(5):
    for num in range(5):
        print("num1: ", num1 , "num: ", num)

#task 5

print("-------------TASK-5-------------")

password = "NIKA"

user_input = input("Please enter your password to Login: ")

while user_input != password:
    user_input = input("Access is denied! Try again: ")

print("Successfully Logined!")