#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/bon-appetit/problem

n, k = map(int, input().split(" "))
l = list(map(int, input().strip().split(" ")))
m = int(input())

Anna = int((sum(l) / 2) - (l[k] * 0.5))
if m == Anna: print("Bon Appetit")
else: print(m - Anna)
