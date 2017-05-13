#! import turtle

import turtle

def tree(branchlen, t):
    if branchlen > 5:
        t.forward(branchlen)
        t.right(30)
        tree(branchlen - 5, t)
        t.left(60)
        tree(branchlen - 5, t)
        t.right(30)
        t.backward(branchlen)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(40, t)
    my_win.exitonclick()

main()

