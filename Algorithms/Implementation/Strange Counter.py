#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/strange-code/problem

x = 10 ** 12
l = [1]
nr = int(input())
while l[-1] < x:
     l.append((l[-1] * 2) + 2)

for i in range(len(l)):
    if l[i] > nr:
        indx = i -1
        break

print(l[indx] + 2 - (nr - l[indx]))
