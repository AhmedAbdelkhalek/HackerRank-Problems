#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

for _ in range(int(input())):
    d = list(map(int, input().strip().split(' ')))
    AtoC = abs(d[0] - d[2])
    BtoC = abs(d[1] - d[2])
    if AtoC < BtoC: print("Cat A")
    elif AtoC > BtoC: print("Cat B")
    else: print("Mouse C")
