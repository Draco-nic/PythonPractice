from random import *
from turtle import *

bgcolor("black")
hideturtle()
speed(0)
width = window_width()
height = window_height()

def star(xpos, ypos):
    size = randrange(1, 6)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")

for x in range(100):
    xpos = randrange(-width/2, width/2)
    ypos = randrange(-height/2, height/2)
    star(xpos, ypos)

done()