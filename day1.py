import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Love Animation")
t.speed(0)
t.hideturtle()

def love(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for i in range(200):
        angle = i / 100 * math.pi
        px = 16 * math.sin(angle) ** 3
        py = 13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle)
        t.goto(x + px * size, y + py * size)
    t.end_fill()

# Animasi detak
for scale in range(1, 10):
    t.clear()
    love(0, 0, scale)
    screen.update()

turtle.done()