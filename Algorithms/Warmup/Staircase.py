#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/staircase/problem

n = int(input().strip())
for i in range(1,n+1):
    print(("#" * i).rjust(n))
