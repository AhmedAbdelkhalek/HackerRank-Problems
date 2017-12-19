#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/manasa-and-stones/problem


for _ in range(int(input())):
    n = int(input()) - 1
    a = int(input())
    b = int(input())

    aSet = set()
    for i in range(n + 1):
        x = ((n - i) * a) + (i * b)
        aSet.add(x)

    print(' '.join(map(str, sorted(aSet))))
