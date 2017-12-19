#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/alternating-characters/problem

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    deletions = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            deletions += 1
    print(deletions)
