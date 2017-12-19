#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/pangrams/problem

# it must fail if the test cases contain non space pangram string.
str = input()
if len(set(str.lower())) == 27: print("pangram")
else: print("not pangram")
