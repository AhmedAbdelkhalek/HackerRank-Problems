#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/counting-valleys/problem

n = input()
s = input()

lvl = 0
hills = 0
for i in s:
    if i == "D" and lvl ==0: hills += 1
    if i == "U": lvl += 1
    if i == "D": lvl -= 1

print(hills)
