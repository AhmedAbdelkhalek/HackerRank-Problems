#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/electronics-shop/problem

s,n,m = input().strip().split(' ')
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))

maxx = -1
for kb in keyboards:
    for d in drives:
        if kb + d > maxx and kb + d <= int(s):
            maxx = kb + d
print(maxx)