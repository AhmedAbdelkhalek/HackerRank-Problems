#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
        # your code goes here
    counter = 0
    subStr = ""
    for char in string:
        counter += 1
        if char not in subStr:
            subStr += char
        if counter % k == 0:
            print(subStr)
            subStr = ""
