#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/diagonal-difference/problem

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

aSum = 0
bSum = 0
for i in range(len(a)):
    aSum += a[i][i]
    bSum += a[i][(i + 1) * -1]

print(abs(aSum-bSum))