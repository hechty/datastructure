#! /usr/bin/env python3
# reverse the characters in a string

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)


    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
def revers(string):
    if type(string) != str:
        return "TypeError"
    li = list(string)
    s = Stack()
    for i in li:
        s.push(i)
    m = Stack()
    while not s.isEmpty():
        m.push(s.pop())
    return "".join(m.items)

s = input("Please input a string:")
print(revers(s))



