from turtle import *

# we want to paint a house

speed(30)
width(7)
color("purple")
shape("turtle")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)


forward(70)
color("yellow")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(135)
forward(141)
left(90)
forward(141)
end_fill()

penup()
goto(130,150)
pendown()

right(135)
forward(40)
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(27)
left(90)
forward(55)
right(90)
forward(28)
right(90)
forward(27)
right(90)
forward(55)



exitonclick()