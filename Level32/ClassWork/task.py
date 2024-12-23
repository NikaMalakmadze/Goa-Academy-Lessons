
#task 1

def opposite(number):
  return -number

print(opposite(1))

#task 2

def repeat_str(repeat, string):
    return string * repeat

print(repeat_str(4, 'a'))

#task 3

def greet():
    return "hello world!"

print(greet())

#task 4

def count_sheeps(sheep):
    return sheep.count(True)

print(count_sheeps([True,  True,  True,  False]))

#task 5

def no_space(x):
    return x.replace(' ', '')

print(no_space("grgrg rgrgr"))

#task 6

def litres(time):
    return time // 2

print(litres(2))