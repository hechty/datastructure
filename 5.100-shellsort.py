#! /usr/bin/env python3
from random import randint
from time import clock


def shellsort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertionsort(alist, startposition, sublistcount)
        sublistcount = sublistcount // 2

def gap_insertionsort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalu = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalu:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalu


def insertion_sort(alist):
    orded_list = alist[:1]
    for i in range(len(alist)-1):
        new_data = alist[i+1]
        orded_list = insertion(new_data, orded_list)
        
    return orded_list

def insertion(new_data, orded_list):
    posi = 0
    for i in range(len(orded_list) - 1, -1, -1):
        if new_data >= orded_list[i]:
            posi = i + 1
            break
    orded_list.insert(posi, new_data)
    return orded_list
alist = [randint(0,3000) for _ in range(1000)]
blist = [randint(0,3000) for _ in range(1000)]
start = clock()
for i in range(10):
    insertion_sort(alist)
end = clock()
print("insertion_sort runningtime:",end-start)
print(alist[:15])
start = clock()
for i in range(10):
    shellsort(blist)
end = clock()
print("shell_sort runningtime:", end - start)
print(blist[:15])
