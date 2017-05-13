#! /usr/bin/env python3


import turtle


my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(myTurtle, linlen):
    if linlen > 0:
        myTurtle.forward(linlen)
        myTurtle.right(90)
        draw_spiral(myTurtle, linlen - 5)

draw_spiral(my_turtle, 100)
my_win.exitonclick()
