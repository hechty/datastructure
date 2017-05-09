#! /usr/bin/env python3

from Dqueue import Dequeue


def pal_checker(a_string):
    check_box = Dequeue()
    for i in list(a_string):
        check_box.add_front(i)
    while check_box.size() > 1 and check_box.peek_front() == check_box.peek_rear():
        print(check_box.remove_front(), check_box.remove_rear())
    if check_box.size() > 1:
        return "This string is Not a Palindrome String"
    else:
        return "This string is a Palindrome String"

def main():
    s = input("Please input a string:")
    print(pal_checker(s))

if __name__ == "__main__":
    main()
       
