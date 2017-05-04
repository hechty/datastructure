#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#有理数加法函数


def rational_plus(a1, b1, a2, b2):
    num = a1 * b2 + a2 * b1
    den = b1 * b2
    return num, den

a1 = 3
b1 = 5
a2, b2 = rational_plus(a1, b1, 7, 10)
print(a2 / b2)
