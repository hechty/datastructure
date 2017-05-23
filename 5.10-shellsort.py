#! /usr/bin/env python3

from time import clock
from random import randint
def insertion_sort(alist):
    orded_list = alist[:1]
    for i in range(len(alist)-1):
        new_data = alist[i+1]
        orded_list = insertion(new_data, orded_list)
    alist = orded_list        

def insertion(new_data, orded_list):
    posi = 0
    for i in range(len(orded_list) - 1, -1, -1):
        if new_data >= orded_list[i]:
            posi = i + 1
            break
    orded_list.insert(posi, new_data)
    return orded_list

def shellsort(alist):
    gap = len(alist) // 2 
    while gap > 0:
        for startposi in range(gap):
            for i in range(startposi + gap, len(alist), gap):
                currposi = i 
                while alist[currposi] < alist[currposi - gap] and currposi - gap >= 0:
                    alist[currposi],alist[currposi - gap] = alist[currposi - gap],alist[currposi]
                    currposi = currposi - gap
        gap = gap // 2
    return alist

ls = [randint(0,1000) for _ in range(1000)]
start = clock()
for i in range(10):
    insertion_sort(ls)
end = clock()
print("insertion_sort runningtime:",end-start)
print(ls[:15])
start = clock()
for i in range(10):
    shellsort(ls)
end = clock()
print("shell_sort runningtime:", end - start)
print(ls[:15])
