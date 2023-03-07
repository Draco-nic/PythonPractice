from turtle import *

speed(0)
move_distance = 20
bgcolor("#C2B280")

color("#006994")

penup()
goto(300, 1000)
pendown()
begin_fill()
goto(2000, 1000)
goto(2000, -1000)
goto(300, -1000)
goto(300, 1000)
end_fill()

penup()
goto(-500, 0)
shape("turtle")
color("green")

def move_up():
    setheading(90)
    forward(move_distance)
    ocean()

def move_down():
    setheading(270)
    forward(move_distance)
    ocean()

def move_left():
    setheading(180)
    forward(move_distance)
    ocean()

def move_right():
    setheading(0)
    forward(move_distance)
    ocean()

def ocean():
    if xcor() > 300:
        hideturtle()
        color("White")
        write("You Win!")

        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")


onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")

listen()
done()