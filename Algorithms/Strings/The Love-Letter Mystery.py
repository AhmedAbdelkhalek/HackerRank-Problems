#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

for _ in range(int(input())):
    s = input()
    res = [abs(ord(s[i]) - ord(s[(i+1)*-1])) for i in range(len(s) // 2)]
    print(sum(res))
    