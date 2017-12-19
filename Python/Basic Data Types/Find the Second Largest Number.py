#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = list(arr)
    F_max = -999999
    S_max = -999999
    for i in arr2:
        if i > F_max:
            S_max = F_max
            F_max = i
        if i > S_max and i != F_max:
            S_max = i
    print(S_max)

