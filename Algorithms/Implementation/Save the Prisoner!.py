#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/save-the-prisoner/problem

for _ in range(int(input())):
    n, m, s = map(int, input().split(" "))
    m = m % n
    m -= 1
    x = s + m
    y = x % n
    # special case if the mod is 0 then we display the last prisoner as n
    if y == 0: y = n
    print(y)