#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/strange-advertising/problem

l = [2]
for _ in range(int(input()) - 1):
    l.append((l[-1] * 3) // 2)
print(sum(l))