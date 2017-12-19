#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def is_beauty(nr, k):
    rv = (int(str(nr)[::-1]))
    if abs(nr - rv) % k == 0: return 1
    return 0

l = list(map(int, input().strip().split(' ')))
print(sum([is_beauty(i, l[2]) for i in range(l[0], l[1] + 1)]))
