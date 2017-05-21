#! /usr/bin/env python3

def short_bubble_sort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum - 1

    return alist

ls = list(input('jjjkk').split())
ls = [int(x) for x in ls] 

print(short_bubble_sort(ls))
