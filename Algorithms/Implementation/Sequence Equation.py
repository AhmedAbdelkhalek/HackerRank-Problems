#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/permutation-equation/problem
n = int(input())
l = list(map(int, input().strip().split(' ')))
for i in range(n):
    q = i + 1
    x2 = l.index(q) + 1
    x3 = l.index(x2) + 1
    print(x3)