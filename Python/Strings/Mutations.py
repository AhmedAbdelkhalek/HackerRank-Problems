#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/python-mutations/problem

aString = input()
x = input().split()
if len(x) ==2 and len(aString)>= int(x[0]):     #trying to add some saftey parameters
    v=list(aString)
    v[int(x[0])] = x[1]
    print(''.join(v))   
