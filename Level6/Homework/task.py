
#task 1

print("-------------TASK-1-------------")

birth_year = int(input("Please enter your birth year: "))

print(f"Your age is: {2024 - birth_year}") if 1900 <= birth_year and birth_year <= 2024 else print(f"You are not Human bro")

#task 2

print("-------------TASK-2-------------")

height = int(input("Please input height of your rectangle: "))

width = int(input("Please input width of your rectangle: "))

area = width * height

perimeter = (width + height) * 2

if width != 0 and height != 0:
    print(f"Area of your rectangle is: {area} units") 
    print(f"Perimeter of your rectangle is: {perimeter} units")
else:
    print("Please enter valid value(s)")

#task 3

print("-------------TASK-3-------------")

distance = int(input("Please input distance from your home to school in kilometers(km): "))

distance_m = distance * 1000

distance_sm = distance * 100000

distance_mm = distance * 1000000

print(f"Distance in meters(m): {distance_m}(m)")
print(f"Distance in centimeters(sm): {distance_sm}(sm)")
print(f"Distance in millimeters(mm): {distance_mm}(mm)")

#task 4

print("-------------TASK-4-------------")

name = input("Please enter your name: ")

last_name = input("Please enter your lastname: ")

mother_name = input("Please enter your mother name: ")

mother_last_name = input("Please enter your mother lastname: ")

father_name = input("Please enter your father name: ")

father_last_name = input("Please enter yout father lastname: ")

fav_color = input("Please enter your favorite color: ")

fav_car = input("Please enter model of your favorite car: ")

hobby1 = input("Please enter your favorite hobbie: ")

hobby2 = input("Please enter your second favorite hobbie: ")

hobby3 = input("Please enter your  third favorite hobbie: ")

print(f"So you are {name} {last_name} Your favorite color is {fav_color}. your favorite car is {fav_car}. your hobbies are: {hobby1}, {hobby2} ,and {hobby3}| your mother is {mother_name} {mother_last_name} | your father is {father_name} {father_last_name}|")

#task 5

print("-------------TASK-5-------------")

num = int(input("Please Enter a two-digit number: "))

units_digit = num % 10

tens_digit = num // 10

digit_sum = units_digit + tens_digit

if num >= 10 and num <= 99:
    print(f"Digits of your two-digit number: {units_digit} and {tens_digit} | Number digits sum is: {digit_sum}")  
else: 
    print("Please enter two-digit number")
