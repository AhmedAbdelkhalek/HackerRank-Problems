#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

input()
l = list(map(int, input().split(" ")))

minScore = 10 ** 9
maxScore = -1
minBreak = maxBreak = -1
for i in l:
    if i > maxScore:
        maxScore = i
        maxBreak += 1
    if i < minScore:
        minScore = i
        minBreak += 1

print(maxBreak,minBreak , sep = " ")
