#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/library-fine/problem

aD, aM, aY = map(int, input().strip().split(" "))  # actuals
eD, eM, eY = map(int, input().strip().split(" "))  # expected
fine = 0
if (aD + (aM - 1) * 12 + (aY - 1) * 365) < (eD + (eM - 1) * 12 + (eY - 1) * 365): pass
elif aY > eY: fine = 10000
elif aM > eM: fine = 500 * (aM - eM)
elif aD > eD: fine = 15 * (aD - eD)
print(fine)
