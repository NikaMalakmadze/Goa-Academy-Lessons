
from turtle import *

def walk():
    forward(200)
    left(90)
    forward(200)

def walk_back():
    left(180)
    forward(200)
    right(90)
    forward(200)

def go_back():
    walk()
    walk_back()

go_back()