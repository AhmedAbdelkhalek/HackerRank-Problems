#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/migratory-birds/problem

from collections import Counter
n = input()
l = list(map(int, input().strip().split(" ")))

maxx = -1
common = 0
for i in range(1, 6):

    if l.count(i) > maxx:
        maxx = l.count(i)
        common = i
print(common)
