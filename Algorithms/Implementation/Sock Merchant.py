#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/sock-merchant/problem

from collections import Counter

n = input()
l = list(map(int, input().strip().split(" ")))

pairs = 0
c = Counter(l)
for i in c.keys():
    pairs += int(c[i] / 2)
print(pairs)
