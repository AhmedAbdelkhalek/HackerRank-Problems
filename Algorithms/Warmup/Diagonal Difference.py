#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/diagonal-difference/problem

# Input a number (not useful, but required to run on hackerrank)
n = int(input().strip())
# create an empty list to store the rows
a = []

for a_i in range(n):
    # each line in the input represents a row, so split it.
    # then loop over columns to covert to int.
    # for more about this syntax search lists comprehension
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    # Now it is a 2D list

# the sum of both diagonals starts with 0
aSum = 0
bSum = 0

# loop over rows to calculate the diagonal
for i in range(len(a)):
    # starts with top left
    aSum += a[i][i]
    # starts with top right
    bSum += a[i][(i + 1) * -1]

# print the absolute difference
print(abs(aSum-bSum))