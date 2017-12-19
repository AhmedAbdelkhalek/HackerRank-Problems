#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

def isRight(txt):
    hackerrank = list("knarrekcah")
    for i in txt:
        # this is necessary, to prevent runtime error when poping an empty list.
        if hackerrank == []: break
        if i == hackerrank[-1]:
            hackerrank.pop()

    if hackerrank == []: print("YES")
    else: print("NO")

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    isRight(s)
