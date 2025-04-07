
# task 1

def greet():
    return "hello world!"

# task 2

def make_upper_case(s):
    return s.upper()

print(make_upper_case("hello"))

# task 3

def repeat_str(repeat, string):
    return string * repeat

print(repeat_str(3, 'hello '))

# task 4

def no_space(x):
    return x.replace(' ', '')

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))

# task 5

def create_array(n):
    res = []
    i=1
    while i<=n: 
        res += [i]
        i += 1
    return res

print(create_array(7),[1,2,3,4,5,6,7])

# task 6

def maps(a):
    return [i*2 for i in a]

print(maps([1, 2, 3]))

# task 7

def grader(s):
    if s > 1 or s < 0.6: return 'F'
    if s >= 0.9: return 'A'
    if s >= 0.8: return 'B'
    if s >= 0.7: return 'C'
    if s >= 0.6: return 'D'

print(grader(0.7))

# task 8

websites = ['codewars']*1000

# task 9

def double_char(s):
    return ''.join(i*2 for i in s)

print(double_char("String"))

# task 10

def people_with_age_drink(age):
    if age < 14: return "drink toddy"
    if age < 18: return 'drink coke'
    if age < 21: return 'drink beer'
    if age >= 21: return 'drink whisky'

print(people_with_age_drink(20))

# task 11

def bonus_time(salary, bonus):
    return "$" + str(salary*10) if bonus else "$" + str(salary)

print(bonus_time(10000, True))

# task 12

def monkey_count(n):
    return [i for i in range(1, n+1)]

print(monkey_count(5))