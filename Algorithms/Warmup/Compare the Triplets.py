#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

# This function takes the the 3 ratings for Alice and Bob
# then return the score for both of them.
def solve(a0, a1, a2, b0, b1, b2):
    # True * 1 = 1 and False * 1 = 0
    # Based on this rule, we get the winner for each phase.
    c1 = ((a0 > b0) * 1) + ((a1 > b1) * 1) + ((a2 > b2) * 1)
    c2 = ((a0 < b0) * 1) + ((a1 < b1) * 1) + ((a2 < b2) * 1)
    # return a tuple with each player score.
    return c1, c2


# accept 3 space separated numbers (in string format)
a0, a1, a2 = input().strip().split(' ')
# convert str to int
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
# call the function and store in the "result" tuple
result = solve(a0, a1, a2, b0, b1, b2)
# map will convert result int type to str, then join the string to display the result as required.
print(" ".join(map(str, result)))


