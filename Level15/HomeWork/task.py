
#task 1

print("-------------TASK-1-------------")

n  = int(input("Please enter number less than 10: "))

print("Your number is less than 10") if n < 10 else print("Your number is greater than 10 or equals to 10 ")

#task 2

print("-------------TASK-2-------------")

num = int(input("Please enter even number:"))

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#task 3

print("-------------TASK-3-------------")

num = int(input("Please enter positive number:"))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")

#task 4

print("-------------TASK-4-------------")

n1 = int(input("Please enter first number:"))
n2 = int(input("Please enter second number:"))

if n1 == n2:
    print("Numbers are same")
else:
    print("Numbers are not same")

#task 5

print("-------------TASK-5-------------")

num = int(input("Please enter your number: "))

if num > 100 and num % 2 == 0:
    print("YES")
else:
    print("NO")

#task 6:

print("-------------TASK-6-------------")

num = int(input("Please enter your number: "))

if num % 5 == 0 or num % 10 == 0:
    print("YES")
else:
    print("NO")

#BOSS LEVEL

print("-------------TASK-BOSS-------------")

layers = int(input("Please enter size of triangle: "))
symbols = 1

for i in range(layers, 0 , -1):
    print(" " * (i - 1) + "*" * symbols)
    symbols += 2

#Boss Difficuly Level

#(|)

print("-------------TASK-BOSS-Difficuly-(|)-----------")

list = []

for i in range(4):
    list.append(input("Enter list element: "))

list.append(None)

for i in range(5):
    print(list[i])

#(||)

print("-------------TASK-BOSS-Difficuly-(||)-----------")

num_list = [9,5,94,711,52,96,71,8]
minimum = num_list[0]

for i in range(len(num_list)):
    if num_list[i] < minimum:
        minimum = num_list[i]

print(f"Minimum Number from list: {minimum}")