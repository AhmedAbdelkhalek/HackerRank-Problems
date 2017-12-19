#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    b = '{0:b}'.format(number)
    w = len(b)+1

    for i in range(1, number + 1):
        print('{0:d}'.format(i).rjust(w-1)+'{0:o}'.format(i).rjust(w)+'{0:X}'.format(i).rjust(w)+'{0:b}'.format(i).rjust(w))


x=int(input())
print_formatted(x)
