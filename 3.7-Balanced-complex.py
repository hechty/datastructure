#! /usr/bin/env python3
# Balanced complex Parentheses by using Stack
from Stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "{[(":
            s.push(symbol)
        else:
            if symbol in "}])":
                if s.isEmpty():
                    balanced = False
                else:
                    matches(s.pop(), symbol)

        index += 1 

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(a, b):
    if a.join(b) in "{}[]()":
        pass
    else:
        balanced = False


s = input("please input parentheses:")
print(parChecker(s))


