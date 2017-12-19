#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/game-of-thrones/problem
from collections import Counter

d = (Counter(input()))
oddFound = False
noPalindrome = False
for i in d.keys():
    if d[i] % 2 == 1 and oddFound:
        noPalindrome = True
        break
    elif d[i] % 2 == 1:
        oddFound = True

if noPalindrome:
    print("NO")
else:
    print("YES")
