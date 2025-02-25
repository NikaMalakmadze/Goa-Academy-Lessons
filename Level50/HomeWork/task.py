
# task 1

print("-------------TASK-1-------------")

def binary_array_to_number(arr):
    return int(''.join(str(i) for i in arr), 2)

print(binary_array_to_number([0,0,1,0]))

# task 2

print("-------------TASK-2-------------")

def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2 == 1

print(lovefunc(2,2))

# task 3

print("-------------TASK-3-------------")

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(is_triangle(7, 2, 2))

# task 4

print("-------------TASK-4-------------")

def longest(a1, a2):
    return ''.join(sorted(set(a1+a2)))

print(longest("aretheyhere", "yestheyarehere"))

# task 5

print("-------------TASK-5-------------")


def invert(lst):
    return [-i for i in lst]

print(invert([1,-2,3,-4,5]))

# task 6

print("-------------TASK-6-------------")

def open_or_senior(data):
    return ['Senior' if age>=55 and cap > 7 else "Open" for (age, cap) in data]

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))

# task 7

print("-------------TASK-7-------------")

def grow(arr):
    mult = 1
    for i in arr:
        mult *= i
    return mult

print(grow([2, 2, 2, 2, 2, 2]))

# task 8

print("-------------TASK-8-------------")

def printer_error(s):
    c = 'abcdefghijklm'
    return f"{len([i for i in s if i not in c])}/{len(s)}"

print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))

# task 9

print("-------------TASK-9-------------")

def dna_to_rna(dna):
    return dna.replace('T', 'U')

print(dna_to_rna("GCAT"))

# task 10

print("-------------TASK-10-------------")

def bmi(weight, height):
    bmi = weight / height**2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
    
print(bmi(100, 1.80))