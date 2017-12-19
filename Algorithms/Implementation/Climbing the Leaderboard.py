#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

input()
scoreBoard = list(map(int, input().strip().split(' ')))
x = (list(set(scoreBoard)))
x = sorted(x, reverse=True)
n = int(input())
AliceScores = list(map(int, input().strip().split(' ')))

arrow = len(x) -1

for i in range(n):
    AliceScore = AliceScores[i]
    lastLeader = x[arrow]
    if lastLeader > AliceScore:
        print(arrow + 2 )
    elif lastLeader == AliceScore:
        print(arrow + 1 )
    elif AliceScore >= x[0]: print(1)
    else:
        while True:
            #print(arrow)
            if arrow < 0: break
            if x[arrow] == AliceScore:
                print(arrow + 1 )
                break
            elif x[arrow] < AliceScore:
                arrow -= 1
            elif x[arrow] > AliceScore:
                print(arrow + 2)
                break
