#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/two-strings/problem
from collections import Counter

n = int(input())
for _ in range(n):
    if len(Counter(input()) & Counter(input())) > 0: print("YES")
    else: print("NO")
    