#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum(n, ar):
    # Complete this function
    aSum = 0
    for i in ar:
        aSum += i
    return aSum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
