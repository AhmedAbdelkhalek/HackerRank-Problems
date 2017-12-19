#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter
d = Counter(input())

def is_frequent(d):
    dd = dict(d)
    zeroFound = False
    for i in dd:
        if dd[i] == 0:
            zeroFound = True
            zeroKey = i
    if zeroFound:
        dd.pop(zeroKey)
    if (max(dd.values()) - min(dd.values())) == 0: return True

frequent = False
if is_frequent(d):
    frequent = True
else:
    for i in d:
        d[i] -= 1
        if is_frequent(d):
            frequent = True
            break
        d[i] += 1

if frequent: print("YES")
else: print("NO")