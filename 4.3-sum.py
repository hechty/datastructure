#! /usr/bin/env python3


def listsum(numlist):
    the_sum = 0
    for i in numlist:
        the_sum = the_sum + i
    return the_sum

print(listsum([1,3,5,7,9]))


def new_sum(numlist):
    if len(numlist) ==1:
        return numlist[0]
    else:
        return numlist[0] + new_sum(numlist[1:])

print(new_sum([1, 3, 5, 7, 9]))

