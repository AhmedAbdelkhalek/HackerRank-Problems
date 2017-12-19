#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/happy-ladybugs/problem
from collections import Counter
def is_happy(b):
    for i in set(b):
        if b.count(i) == 1 and i != '_':
            return 'NO'
        elif i == '_' and b.count(i) == len(b):
            return 'YES'
    if b.count('_') == 0:
        for i in range(1,len(b)-1):
            if b[i] != b[i+1] and b[i] != b[i-1]:
                return 'NO'
    return 'YES'

for _ in range(int(input())):
    input()
    print(is_happy(input()))
