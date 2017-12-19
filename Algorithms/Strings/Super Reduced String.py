#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/reduced-string/problem


import sys


def reduce_str(str):
    if str == "":
        return "Empty String"
    for i in range(len(str)):
        if str[i:i + 2] == str[i] * 2:
            return reduce_str(str[:i] + str[i + 2:])
    return str


s = input().strip()
print(reduce_str(s))
