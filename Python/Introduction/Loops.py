#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input())
    if n <21:
        for i in range(n):
            print(i*i)
