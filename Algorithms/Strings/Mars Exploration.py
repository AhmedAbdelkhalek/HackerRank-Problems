#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/mars-exploration/problem

import sys

msg = input().strip()
counter = 0

for i in range(0, len(msg), 3):
    if msg[i + 0] != "S": counter += 1
    if msg[i + 1] != "O": counter += 1
    if msg[i + 2] != "S": counter += 1
print(counter)
