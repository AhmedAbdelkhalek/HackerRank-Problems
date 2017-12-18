#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/staircase/problem

# enter the number of rows required
n = int(input().strip())

# starts with 1 and compensate with n+1
for i in range(1,n+1):
    # print the # right aligned.
    print(("#" * i).rjust(n))
