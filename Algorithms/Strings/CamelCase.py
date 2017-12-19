#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/camelcase/problem

import sys

s = input().strip()
c = 1
for i in s:
    if ord(i) <= 90 and ord(i) >= 65:
        c += 1

print(c)
