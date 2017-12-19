#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/sherlock-and-array/problem

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    theRest = sum(l)
    onLeft = 0
    for i in l:
        theRest  -= i
        if onLeft == theRest:
            print("YES")
            break
        onLeft += i
    else:
        print("NO")
