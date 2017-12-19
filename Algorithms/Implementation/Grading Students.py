#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/grading

def round_to_five(n):
    for i in range(6):
        if (n + i) % 5 == 0: return (n + i)

n = int(input())
for _ in range(n):
    x = int(input())
    y = round_to_five(x)
    if x < 38: print(x)
    elif y - x < 3: print(y)
    else: print(x)