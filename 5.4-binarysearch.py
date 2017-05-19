#! /usr/bin/env python3


def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        if alist[len(alist)//2] > item:
            alist = alist[:len(alist)//2]
        elif alist[len(alist)//2] == item:
            return True
        else:
            alist = alist[len(alist)//2+1:]
    return binary_search(alist, item)

alist = input("ALIST:").split()
alist = [int(x) for x in alist]
item = int(input("input a item to find:"))
print(binary_search(alist, item))


