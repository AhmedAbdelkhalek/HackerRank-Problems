#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem


def minSteps(n, B):
    count = 0
    for i in range(n-2):
        if B[i:i+3] == list("010"):
            B[i+2] = 1
            count += 1
    return count

n = int(input().strip())
B = list(input().strip())
result = minSteps(n, B)
print(result)
