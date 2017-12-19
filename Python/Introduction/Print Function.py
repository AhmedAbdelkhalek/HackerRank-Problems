#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    txt = ""
    for i in range(n):
        txt += str(i + 1)

    print(txt)
