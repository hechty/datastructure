#! /usr/bin/env python3


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

ls = input("input a list of num: ").split()
ls = [int(x) for x in ls]

sorted_ls = insertion_sort(ls)

print(sorted_ls)
