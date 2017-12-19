#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
U = set()
lastLetter = ""
for i in range(len(s)):
    if s[i] != lastLetter:
        U.add(ord(s[i]) - 96)
        repeat = 1
        lastLetter = s[i]
    else:
        repeat += 1
        U.add(repeat * (ord(s[i]) - 96))

n = int(input().strip())
for a0 in range(n):
    x = int(input().strip())
    if x in U:
        print("Yes")
    else:
        print("No")


