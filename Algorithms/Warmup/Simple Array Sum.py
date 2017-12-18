#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/simple-array-sum/problem

# a function the accepts a list and return the sum of this list
def simpleArraySum(n, ar):
    # the sum starts with 0
    aSum = 0
    # loop over each item in the array
    for i in ar:
        # add the element to the current sum.
        # sum starts with 0 and keep increasing in each loop
        aSum += i
    return aSum

# Input a number (not useful, but required to run on hackerrank)
n = int(input().strip())
# Convert space delimited numbers to list of ints
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
# print the sum.
print(result)
