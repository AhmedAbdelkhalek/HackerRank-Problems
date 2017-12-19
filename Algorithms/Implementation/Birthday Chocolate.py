#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/the-birthday-bar/problem

input()
l = list(map(int, input().strip().split(" ")))
dm = list(map(int, input().split(" ")))
d = dm[0]
m = dm[1]

counter = 0
for i in range(len(l) - m + 1 ):
    if sum(l[i:i + m]) == d:
        counter += 1
print(counter)