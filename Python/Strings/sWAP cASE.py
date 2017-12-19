#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    t =[]
    for i in s:
        if i.islower():
            t.append( i.upper())
        else:
            t.append(i.lower())
    print(''.join(t))


swap_case(input())
