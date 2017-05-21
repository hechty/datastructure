#! /usr/bin/env python3

from time import time
from random import randint
from collections import OrderedDict

players = list('abcdefg')
start = time()
d = OrderedDict()
for i in range(7):
    input()
    p = players.pop(randint(0, 6-i))
    end = time()
    print(i+1, p, end - start)
    d[p] = end - start
print('*'*30)
for i in d:
    print(i,' ',d[i])



