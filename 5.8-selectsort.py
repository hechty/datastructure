#! /usr/bin/env python3

def selection_sort(alist):
    positionmax = 0
    step = len(alist) - 1
    for i in range(step):
        listlen = step + 1 - i
        for j in range(listlen):
            if alist[j] > alist[positionmax]:
                positionmax = j
        alist[positionmax], alist[listlen-1] = alist[listlen-1], alist[positionmax] 
    return alist

ls = list(input('jjjkk').split())
ls = [int(x) for x in ls] 

print(selection_sort(ls))
