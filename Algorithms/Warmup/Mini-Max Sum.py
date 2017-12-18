#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/mini-max-sum/problem

arr = list(map(int, input().strip().split(' ')))
arr = sorted(arr)
print("{} {}".format( sum(arr[:4]), sum(arr[1:])))

