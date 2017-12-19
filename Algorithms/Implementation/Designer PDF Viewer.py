#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

k = list(map(int, input().strip().split(' ')))
s = input()

talls = [k[ord(c) - 97] for c in s]
print(max(talls) * len(s))

