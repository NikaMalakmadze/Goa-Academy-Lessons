
#task 1

print("-------------TASK-1-------------")

from turtle import *

def triangle(clr):
    color(clr)
    for _ in range(3):
        forward(200)
        left(120)

def triangle_color(num):
    for i in range(num):
        if i % 2 == 1:
            triangle("green")
            print(i , "Green")
        else:
            triangle("blue")
            print(i , "Blue")


triangle_color(120)
exitonclick()

#task 2

print("-------------TASK-2-------------")

def hello_world(name):
    print(f"Hello World and {name}!")

hello_world("nika")

#task 3

print("-------------TASK-3-------------")

def even_or_odd(number):
    print(f"This number({number}) is odd") if number % 2 == 1 else print(f"This number({number}) is even")

even_or_odd(23)
even_or_odd(30)

#task 4

def rectangle():
    for _ in range(3):
        print("******")

def tree():
    symbols = 3
    print(" " * 5, "*")
    for i in range(4, -1 , -2):
        print(" " * i , "*" * symbols)
        symbols += 4
    print(" " * 5, "*")
    print(" " * 5, "*")

def rhombus():
    for i in range(4):
        print(" " * i, "*" * 5)

def repeat_figures():
    for _ in range(120):
        rectangle()
        tree()
        rhombus()

repeat_figures()
