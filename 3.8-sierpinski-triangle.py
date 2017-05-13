#! /usr/bin/env python3
import turtle

def sie_triangle(x, y, r, t):
    t.up()
    t.goto(x, y)
    t.down()
    t.right(90)
    t.forward(r / 2)
    t.left(120)
    t.forward(r)
    t.left(120)
    t.forward(r)
    t.left(120)
    t.forward(r / 2)
    t.left(60)
    t.fillcolor("green")
    t.begin_fill()
    t.forward(r / 2)
    t.left(120)
    t.forward(r / 2)
    t.left(120)
    t.forward(r / 2)
    t.left(150)
    t.end_fill()
    if r > 30:
        sie_triangle(x + r / 4, y, r / 2, t)
        sie_triangle(x - r / 4, y, r / 2, t)
        sie_triangle(x, y + 0.433 * r, r / 2, t)

def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    t.left(90)
    sie_triangle(0, 0, 150, t)

    s.exitonclick()

main()
