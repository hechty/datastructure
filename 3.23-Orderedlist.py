#! /usr/bin/env python3


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current.get_data() != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def add(self, item):
        current = self.head
        previous =None
        while item > current.get_data() and not current.is_empty():
            previous = current
            current = current.get_next()
        if current == None:
            temp = Node(item)
            previous.set_next(temp)
        elif previous == None:
            temp = Node(item)
            self.head = temp
            temp.set_next(current)


