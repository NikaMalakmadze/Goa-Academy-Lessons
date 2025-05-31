
# task 1

try:
    num1 = float(input("Enter First Num: "))
    num2 = float(input("Enter Second Num: "))
    
    result = num1 / num2
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print("Error: Can't Divide by 0")
except ValueError:
    print("Error: Enter only Numbers!")

# task 2

def check_age(age):
    if age <= 0: raise ValueError('Age Must be Greater Than 0')
    print(f'Inputed Age: {age}')

try:
    input_age = int(input("შეიყვანე ასაკი: "))
    check_age(input_age)
except Exception as e:
    print(f'Error: {e}')
