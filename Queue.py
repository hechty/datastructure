#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#Implementing A Queue In Python


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def main():
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.dequeue()
    print(s.size())
    print(s.isEmpty())
    print(s.items)
    print(s)

if __name__ == '__main__':
    main()
