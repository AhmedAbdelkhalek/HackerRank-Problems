#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/whats-your-name/problem


def print_full_name(a, b):
    # print("Hello " +a +" "+ b+"! You just delved into python.")
    print("Hello {} {}! You just delved into python.".format(a, b))


fn = input()
ln = input()
print_full_name(fn, ln)
