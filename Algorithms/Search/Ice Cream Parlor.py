#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/icecream-parlor/problem

for _ in range(int(input())):
    m = int(input())
    input()
    prices = list(map(int, input().split()))
    # prices = sorted(prices)
    found = False
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] == m:
                print(i + 1, j + 1, sep=" ")
                found = True
                break
        if found: break

