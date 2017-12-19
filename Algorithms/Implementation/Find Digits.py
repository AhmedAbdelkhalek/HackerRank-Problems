#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/find-digits/problem

for _ in range(int(input())):
    nr = input()
    print(sum([1 for i in nr if i != "0" and int(nr) % int(i)  == 0]))