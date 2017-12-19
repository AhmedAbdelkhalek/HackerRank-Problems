#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/two-characters/problem

import sys


def valid_t(str):
    chrSet = set()
    chrSet.add(str[-1])
    for i in range(len(str) - 1):
        chrSet.add(str[i])
        if len(chrSet) > 2:
            return False
        if str[i] == str[i + 1]:
            return False
    return True


def find_longest(str):
    if len(str) == 1:
        return ""
    set_of_str = list(set(str))
    longest_str = ""
    for i in range(len(set_of_str)):
        for j in range(len(set_of_str)):
            str_copy = str[:]
            for k in range(len(set_of_str)):
                if k != i and k != j:
                    str_copy = str_copy.replace(set_of_str[k], "")
            if valid_t(str_copy) and len(str_copy) > len(longest_str):
                longest_str = str_copy[:]

    return longest_str


s_len = int(input().strip())
s = input().strip()
print(len(find_longest(s)))
