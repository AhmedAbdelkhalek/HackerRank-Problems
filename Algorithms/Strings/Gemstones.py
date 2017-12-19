#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/gem-stones/problem

import sys
def gem_in_all_stones(letter, arr):
    for i in arr:
        if letter not in i: return 0
    return 1

def gemstones(arr):
    total = 0
    for i in range(97,123):
        total += gem_in_all_stones(chr(i), arr)
    return total

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)
