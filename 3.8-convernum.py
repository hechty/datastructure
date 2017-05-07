#! /usr/bin/env python3
#3.8 Converting DecimalNumbers to binary Numbers
from Stack import Stack

def divideBy2(decNumber, base):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binString = ''
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString

s = int(input("Input a number:"))
b = int(input('Input base:'))
print(b, "Based Number Is:",divideBy2(s, b))


