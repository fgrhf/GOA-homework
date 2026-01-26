from turtle import *


#we want to paint a house

#step 1: draw a suare

speed(40)

width(5)
color("brown")

forward(200)
left(90)

forward(200)
left(90)
     
forward(200)   
left(90)

forward(200)
left(90)
#end of square

#drowing a door


forward(70)
color("black")
begin_fill()
left(90)
forward(90)      # height of the door
right(90)
forward(60)
right(90)
forward(90)
end_fill()

penup()
goto(200, 200)
pendown()

color("gray")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(0, 160)
pendown()
color("blue")
begin_fill()
right(240)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(200, 160)
color("blue")
begin_fill()
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(200, 200)
pendown()
color("purple")
begin_fill()
left(90)
forward(150)
left(90)
forward(40)
left(90)
forward(76)
end_fill()


exitonclick()
