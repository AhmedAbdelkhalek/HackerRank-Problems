#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/mini-max-sum/problem

# Convert space delimited numbers to list of ints
arr = list(map(int, input().strip().split(' ')))
# Sort the list
arr = sorted(arr)

# Print the sum of the first and last 4 numbers separated by a space.
print("{} {}".format(sum(arr[:4]), sum(arr[1:])))
