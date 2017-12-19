#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

n, k = map(int, input().split(" "))
l = list(map(int, input().strip().split(" ")))

counter = 0
for i in range(n):
    for j in range(n):
        if i < j and ( (l[i] + l[j])% k) == 0:
            counter += 1

print(counter)