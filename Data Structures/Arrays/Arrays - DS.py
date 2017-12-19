#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/arrays-ds/problem


n = int(input())
y = (input().split())
x = ''
for i in range(n):
    x = y[i] + ' ' + x
print(x)
