#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    seconds = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])
        scores.add(score)

    seconds = [i[1] for i in students if i[0] == sorted(scores)[1]]
    print("\n".join(sorted(seconds)))
