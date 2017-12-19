#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/between-two-sets/problem

input()
# l1 = list(input().split(" "))
l1 = list(map(int, input().split(" ")))
l2 = list(map(int, input().split(" ")))

count = 0
for x in range(min(l1 + l2), max(l1 + l2)+1):
    noWay = False
    for a in l1:
        if x % a != 0:
            noWay = True
            break

    if noWay: continue
    for b in l2:
        if b % x != 0:
           noWay = True
           break
    if noWay: continue
    count += 1

print(count)