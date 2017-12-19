#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/python-lists/problem

aList = []
lines = []
nrOflines = int(input())
for i in range(nrOflines):
    line = input()
    if line:
        lines.append(line)

for j in lines:
    x = j.split(' ')
    if x[0] == "insert":
        aList.insert(int(x[1]),int(x[2]))
    elif x[0] == "print":
        print(aList)
    elif x[0] == "remove":
        aList.remove(int(x[1]))
    elif x[0] == "append":
        aList.append(int(x[1]))
    elif x[0] == "sort":
        aList.sort()
    elif x[0] == "pop":
        aList.pop()
    elif x[0] == "reverse":
        aList.reverse()


