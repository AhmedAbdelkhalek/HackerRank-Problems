#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

print(ar.count(max(ar)))
