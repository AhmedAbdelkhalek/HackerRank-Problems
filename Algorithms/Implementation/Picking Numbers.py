#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/picking-numbers/problem

input()
d = list(map(int, input().strip().split(' ')))
maxx = 0
for i in range(max(d)):
    c = d.count(i) + d.count(i+1)
    if c > maxx: maxx = c

print(maxx)