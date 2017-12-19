#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/missing-numbers/problem

from collections import Counter

input()
A = Counter(list(map(int, input().split())))
input()
B = Counter(list(map(int, input().split())))

print(' '.join(map(str, sorted(list(B - A)))))

