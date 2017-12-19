#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # your code goes here
    arr = set(array)
    return sum(arr)/len(arr)
