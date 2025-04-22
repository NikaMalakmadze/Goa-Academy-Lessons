
#task 1

print("-------------TASK-1-------------")

age = int(input("Please Enter your age: "))

for i in range(age + 1):
    print(i)

#task 2

print("-------------TASK-2-------------")

Temp_C = float(input("Enter the Temperature: "))

Temp_F = round((Temp_C * 1.8 ) + 32 , 1)

print(f"Temperature in Fahrenheit is: {Temp_F} °F")   

#task 3

print("-------------TASK-3-------------")

a = 5
b = 10
c = 8

print(f"a = {a} b = {b} c = {c}")

print(f"a > b answer: {a > b}")
print(f"c < b answer: {c < b}")
print(f"a > c answer: {a > c}")

T = True
F = False

print(f"T and F answer: {T and False}")
print(f"T or F answer: {T or False}")
print(f"not T and F answer: {not T and False}")

#task 4

print("-------------TASK-4-------------")

n = int(input("Please Enter size of Triangle: "))

for i in range(1 , n + 1):
    print("*" * i)

#task 5

print("-------------TASK-5-------------")

your_age = int(input("Please enter your age: "))

check = your_age == 20

print(f"are you twenty years old? ANSWER: {check}")