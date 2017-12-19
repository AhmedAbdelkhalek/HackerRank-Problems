#!/bin/python3
# Easy
#https://www.hackerrank.com/challenges/circular-array-rotation/problem
from collections import deque

n, k, q = map(int, input().strip().split(" "))
x = deque(map(int, input().strip().split(' ')))
x.rotate(k)

for _ in range(q):
    print(x[int(input())])

