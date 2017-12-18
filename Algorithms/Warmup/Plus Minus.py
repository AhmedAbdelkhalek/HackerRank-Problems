#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/plus-minus/problem

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pCount = nCount = zCount = 0
for i in arr:
    if i > 0:
        pCount += 1
    elif i < 0:
        nCount += 1
    else:
        zCount += 1

print("{0:.6f}".format(pCount/ (pCount + nCount + zCount)))
print("{0:.6f}".format(nCount/ (pCount + nCount + zCount)))
print("{0:.6f}".format(zCount/ (pCount + nCount + zCount)))