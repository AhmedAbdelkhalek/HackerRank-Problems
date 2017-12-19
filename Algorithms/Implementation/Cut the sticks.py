#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/cut-the-sticks/problem

input()
l = list(map(int, input().strip().split(' ')))
minus = min(l)
print(len(l))
while True:
    b = [i - minus for i in l if i - minus > 0]
    l = b[:]
    if len(b) == 0: break
    print(len(b))
    minus = min(b)
