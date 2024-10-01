
#task 1

print("-------------TASK-1-------------")

age = int(input("Please input your age: "))

check_age = 13 < age < 19

print(f"Is your age between 13 and 19? answer: {check_age}")

#task 2

print("-------------TASK-2-------------")

marks = int(input("Please enter your mark(1-10): "))

if 1 <= marks <= 10:
    
    is_A = marks >= 9
    is_B = 8 <= marks < 9
    is_C = 7 <= marks < 8
    is_D = 6 <= marks < 7
    is_F = marks < 6

    print("Your score:")
    print(f"Your score is A: {is_A}")
    print(f"Your score is B: {is_B}")
    print(f"Your score is C: {is_C}")
    print(f"Your score is D: {is_D}")
    print(f"Your score is F: {is_F}")
else:
    print("Out of range!")

#task 3

print("-------------TASK-3-------------")

true_variable = True
false_variable = False

print("Logical Operators: ")
print(f"True and False is: {true_variable and false_variable}")
print(f"True or False is: {true_variable or false_variable}")
print(f"Not True is:: {not true_variable}")
print(f"Not False is: {not false_variable}")

#task 4

print("-------------TASK-4-------------")

num1 = int(input("Please enter first num: "))
num2 = int(input("Please enter Second num: "))

print(f"Does first number = Second number? answer: {num1 == num2}")
print(f"Does first number > Second number? answer: {num1 > num2}")
print(f"Does first number < Second number? answer: {num1 < num2}")
print(f"Does first number >= Second number? answer: {num1 >= num2}")
print(f"Does first number <= Second number? answer: {num1 <= num2}")
print(f"Does first number != Second number? answer: {num1 != num2}")

#task 5

print("-------------TASK-5-------------")

a = 43
b = 35
c = 12

is_a_greatest = a > b > c
is_b_middle = c < b < a
is_c_least = c < b < a

print(f"Is a biggest? answer: {is_a_greatest}")
print(f"Is b middle? answer: {is_b_middle}")
print(f"is c least? answer: {is_c_least}")

#task 6

print("-------------TASK-6-------------")

score = int(input("Please neter your test score(0-100): "))

is_pass = score >= 50
is_high_pass = 75 <= score < 90
is_perfect = score == 100
is_failing = score < 50

print(f"Your score is pass: {is_pass}")
print(f"Your score is high pass: {is_high_pass}")
print(f"Your score is perfect: {is_perfect}")
print(f"Your score is failing: {is_failing}")

#task 7

print("-------------TASK-7-------------")

P = True
Q = False

P_and_not_Q = P and not Q
not_P_and_Q = not P and Q
P_xor_Q = not P or not Q

print(f"P_and_not_Q : {P_and_not_Q}")
print(f"not_P_and_Q : {not_P_and_Q}")
print(f"P_xor_Q : {P_xor_Q}")
