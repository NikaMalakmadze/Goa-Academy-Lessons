
#task 1

print("-------------TASK-1-------------")

name = input()
result = ""

for i in name:
    result += i + " "
print(result)

#task 2

print("-------------TASK-2-------------")

a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))

for i in range(a, b):
    if i % 2 == 0 and i % 3 == 0:
        print(i , "This number is multiple of 6")
    else:
        print(i)

#task 3

print("-------------TASK-3-------------")

result = 0

for i in range(5):
    num = float(input(f"Please enter {i + 1} number: "))
    result += num

average = result / 5

print("Arithmetic average of these numbers: " , average)

#task 4

print("-------------TASK-4-------------")

for i in range(-100 , 100):
    if i > 0:
        print(i)

#task 5

print("-------------TASK-5-------------")

number = float(input("Please enter a positive number: "))

while number >= 0:
    number = float(input("Please enter a positive number: "))
print("While loop ended!")

#BOSS LEVEL

print("-------------TASK-BOSS-------------")

triangle_size = int(input("Please enter size of triangle: "))
triangle_base = triangle_size * 2
spaces = triangle_base - 2

for i in range(1 , triangle_size + 1):
    print("*" * i + " " * spaces + "*" * i)
    spaces -= 2
