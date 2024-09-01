from turtle import *

speed(100) #speed control

#background
penup()
goto(100,-150)
pendown()
color("yellow")
begin_fill()
circle(300)
end_fill()

#background outline
width(7)
color("black")
circle(300)

#house square
penup()
goto(0,0)
pendown()
color("#DD8C1F") # brick color
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

#house door
forward(50)
left(90)
color("#5F6666")  # door color
begin_fill()
forward(120)  # door height
right(90)
forward(50)   # door width
right(90)
forward(120)
end_fill()

#house roof
penup()
goto(0,200)
pendown()
color("#0BE634") #roof color
begin_fill()
left(150)
forward(200)
right(120)
forward(200)
end_fill()

#house window
penup()
goto(120, 120)
pendown()
color("#11FFF2") #window color
begin_fill()
left(60)
forward(50)  #window height and width
right(90)
forward(50)  #window height and width
right(90)
forward(50)  #window height and width
right(90)
forward(50)  #window height and width
right(90)
end_fill()

# #house outline
penup()
goto(0,0)
pendown()
color("black")
width(7)
setheading(0)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

# door outline
forward(50)
left(90)
forward(120)  # door height
right(90)
forward(50)   # door width
right(90)
forward(120)

#roof outline
penup()
goto(0,200)
pendown()
left(150)
forward(200)
right(120)
forward(200)

#window outline
penup()
goto(120, 120)
pendown()
left(60)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
penup()
goto(120, 95)
pendown()
left(90)
forward(50)

#door handle
penup()
goto(70, 50)
pendown()
forward(5)
right(90)
forward(5)
right(90)
forward(5)
right(90)
forward(5)
right(90)

#roof window
penup()
goto(100, 250)
pendown()
width(1)
color("#11FFF2")
begin_fill()
circle(20)
end_fill()
color("black")
width(7)
circle(20)

exitonclick()