#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import sys

n = int(input().strip())
s = input().strip()
k = int(input().strip())

newS = ""


def letters_shifter(letter, start, end, shift):
    # if k = 4
    # X -> B  ( 88 - > 66)
    # 88 + 2 = 90 remaining 2
    # 65 + 2   - 1 (to get the correct letter)
    # chr(66) = "B"
    if ord(letter) >= start and ord(letter) <= end:
        nr = ord(letter) + shift
        if nr > end:
            nr = start + (nr - end) - 1
        return chr(nr)
    else:
        return letter


for i in s:
    lett = letters_shifter(i, 65, 90, k % 26)
    lett = letters_shifter(lett, 97, 122, k % 26)
    newS += lett
print(newS)
