#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    c1 = ((a0 > b0) * 1) + ((a1 > b1) * 1) + ((a2 > b2) * 1)
    c2 = ((a0 < b0) * 1) + ((a1 < b1) * 1) + ((a2 < b2) * 1)
    return c1, c2


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))


