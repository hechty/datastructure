#! /usr/bin/env python3

from random import randint

def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)

def quick_sort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quick_sort_helper(alist, first, splitpoint-1)
        quick_sort_helper(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1

        if leftmark > rightmark:
            done = True
        else:
            alist[rightmark],alist[leftmark] = alist[leftmark], alist[rightmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark

alist = [randint(0,100) for _ in range(50)]
quick_sort(alist)
print(alist)
