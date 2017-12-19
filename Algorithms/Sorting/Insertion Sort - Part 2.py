#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/insertionsort2/problem

def insertionSort(l):
    for i in range(1, len(l)):
        curNum = l[i]
        for j in range(i - 1, -1, -1):
            if l[j] > curNum:
                l[j + 1] = l[j]
                # print(" ".join(map(str,l )))
                if j == 0: l[j] = curNum
                if l[j-1]  < curNum: l[j] = curNum

            # else:
            #     break
        # l[j + 1] = curNum
        print(" ".join(map(str, l)))

input()
l = list(map(int, input().split()))
# l = [2, 4, 6, 8, 3]
insertionSort(l)
