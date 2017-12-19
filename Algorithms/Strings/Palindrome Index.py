#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/palindrome-index/problem

def is_palindrome (s):
    mid = len(s) // 2
    if  s[:mid] == s[mid * -1:][::-1]: return True
    else: return False

for _ in range(int(input())):
    s = input()
    if is_palindrome(s):
        print(-1)
    else:
        for i in range(len(s)):
            if is_palindrome(s[:i] + s[i+1:]):
                print(i)
                break

