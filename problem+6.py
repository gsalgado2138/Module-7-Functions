#giovanni salgado
#11/14/2021
#problem 6
# Use the following chunk of code as a base to produce the image shown below.

import turtle
def drawsquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        t.hideturtle()

wn = turtle.Screen()

alex = turtle.turtle()
alex.color('red')
size = 20

for i in range(5):
    drawsquare(alex, size)
    size = size + 20
    alex.penup()
    alex.goto(alex.pos() + (-10, -10))
    alex.pendown()
    wn.exitonclick()