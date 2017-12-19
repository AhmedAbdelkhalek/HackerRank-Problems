#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/angry-professor/problem

for _ in range(int(input())):
    l1 = list(map(int, input().strip().split(' ')))
    l2 = list(map(int, input().strip().split(' ')))

    x = sum([1 for i in l2 if i <= 0])
    if x >= l1[1]: print("NO")
    else: print("YES")
