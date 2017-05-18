#! /usr/bin/env python3


def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

testlist = input("Please in put a list,split by space:").split()
testlist = [int(x) for x in testlist]
item = int(input("PLEASE INPUT TESTNUM:"))
print(binary_search(testlist, item))
