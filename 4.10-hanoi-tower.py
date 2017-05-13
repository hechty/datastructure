#! /usr/bin/env python3
# -*-coding:utf-8-*-

from Stack import Stack

step = 0
def hanoi(n, A, B, C):
    global step
    if n < 1:
        return
    else:
        hanoi(n-1, A, C, B)
        step += 1
        print("第 {:^10d} 步: 移动 {:^4d} 号盘子到 {} 号杆".format(step,n,C))
        hanoi(n-1, B, A, C)
        
s = int(input("请输入汉诺塔阶数:"))
hanoi(s, "1", "2", "3")
print("{:^4d} 阶汉诺塔盘,需要移动 {:^20d} 步".format(s, step)) 
