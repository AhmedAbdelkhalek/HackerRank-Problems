#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/the-hurdle-race/problem

k = list(map(int, input().strip().split(' ')))
d = list(map(int, input().strip().split(' ')))

print(max(0, max(d) - k[1]))