#! /usr/bin/env python3
# stack in python 
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        print(len(self.items)
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    

