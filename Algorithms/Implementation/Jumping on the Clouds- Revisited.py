#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
n, k = map(int, input().strip().split(" "))
l = list(map(int, input().strip().split(' ')))

energy = 100
newLocation = 0
while True:
    newLocation = (newLocation + k) % n
    energy -= (1 + (l[newLocation] * 2))
    if newLocation == 0: break
print(energy)
