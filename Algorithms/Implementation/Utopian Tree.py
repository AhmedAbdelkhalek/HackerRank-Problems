#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/utopian-tree/problem

for _ in range(int(input())):
    ss = int(input())

    if ss% 2 == 1:
        s = ss +1
    else:
        s = ss
    x = (s / 2) + 1
    y = (2 ** x ) - 1
    if ss % 2 == 0:
        print(int(y))
    else:
        print(int(y - 1))
