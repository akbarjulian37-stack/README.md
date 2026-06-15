import turtle
import math

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.color("red", "red")
t.speed(0)
t.pensize(2)

def love_curve(t, size):
    for i in range(200):
        t.right(1)
        t.forward(size * math.sin(math.radians(i)) * 0.1)

t.penup()
t.goto(0, -150)
t.pendown()
t.begin_fill()

love_curve(t, 200)
t.left(120)
love_curve(t, 200)

t.end_fill()
t.hideturtle()

t.penup()
t.goto(0, 50)
t.color("white")
t.write("I Love You", align="center", font=("Arial", 24, "bold"))

turtle.done(1)