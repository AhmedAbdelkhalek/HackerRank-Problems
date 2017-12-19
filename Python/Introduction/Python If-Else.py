#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/py-if-else/problem

if __name__ == '__main__':
    n = int(input())
    if n % 2 == 1:
        txt = "Weird"
    elif n % 2 == 0 and n > 20:
        txt = "Not Weird"
    elif n == 2 or n == 4:
        txt = "Not Weird"
    else:
        txt = "Weird"

    print(txt)
