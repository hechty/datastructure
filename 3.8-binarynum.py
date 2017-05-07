#! /usr/bin/env python3
#3.8 Converting DecimalNumbers to binary Numbers
from Stack import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString

s = int(input("Input a number:"))
print("Binary Number Is",divideBy2(s))


