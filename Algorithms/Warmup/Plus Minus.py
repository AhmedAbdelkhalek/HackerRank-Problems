#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/plus-minus/problem

# Input the number of items in the list
n = int(input().strip())
# Convert space delimited numbers to list of ints using list comprehension
l = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pCount = nCount = zCount = 0
# loop over the elements in the list
for i in l:
    # if the item > 0, increase the positive count by 1
    if i > 0:
        pCount += 1
    # if the item < 0, increase the positive count by 1
    elif i < 0:
        nCount += 1
    # if the item = 0, increase the zeros count by 1
    else:
        zCount += 1

# A decimal representing of the fraction of positive numbers in the array compared to its size.
print("{0:.6f}".format(pCount/ n))
# A decimal representing of the fraction of negative numbers in the array compared to its size.
print("{0:.6f}".format(nCount/ n))
# A decimal representing of the fraction of zeroes in the array compared to its size.
print("{0:.6f}".format(zCount/ n))
