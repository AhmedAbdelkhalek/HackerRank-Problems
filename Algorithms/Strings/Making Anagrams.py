#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

d1 = Counter(input())
d2 = Counter(input())
result = 0
for i in d1.keys():
    if i in d2:
        result += (min(d1[i], d2[i]) * 2)
print(sum(d1.values()) + sum(d2.values()) - result)
