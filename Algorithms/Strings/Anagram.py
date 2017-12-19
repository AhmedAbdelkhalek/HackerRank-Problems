#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter
n = int(input())
for _ in range(n):
    test = input()
    length = len(test)
    if len(test) % 2 != 0:
        print("-1")
    else:
        diff = Counter(test[:length//2]) - Counter(test[length//2:])
        print(sum(diff.values()))
