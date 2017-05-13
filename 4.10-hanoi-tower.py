#! /usr/bin/env python3

from Stack import Stack

step = 0
def hanoi(n):
    global step
    if n < 2:
        r1 = "MOVE 1 TO OTHER"
        step += 1
        print("STEP: ",step,"    ",end='')
        print(r1)
        return
    else:
        hanoi(n-1)
        step += 1
        print("STEP: ",step,"    ",end='')
        print("Move", n,"TO B/C")
        hanoi(n-1) 
        
s = int(input("input a num:"))
hanoi(s)
print("Move {} disks,Using {} Step".format(s, step)) 
