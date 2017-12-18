#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

# Input a number (not useful, but required to run on hackerrank)
n = int(input().strip())
# Convert space delimited numbers to list of ints
ar = list(map(int, input().strip().split(' ')))

# print the number of times the maximum of the list appeared in the list
print(ar.count(max(ar)))
