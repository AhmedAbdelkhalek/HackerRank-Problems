#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/drawing-book/problem

nPages = int(input())
page = int(input())
print(min(page // 2, (nPages // 2) - (page // 2)))
