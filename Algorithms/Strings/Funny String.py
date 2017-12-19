#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(str):
    s = list(str)
    r = list(reversed(str))
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"
    return "Funny"


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
