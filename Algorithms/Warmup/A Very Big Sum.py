#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/a-very-big-sum/problem

# Input a number (not useful, but required to run on hackerrank)
n = int(input().strip())
# Convert space delimited numbers to list of ints
ar = list(map(int, input().strip().split(' ')))

# Print the sum of the list
print(sum(ar))
