#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    for i, j in enumerate(s):
        break_it = False
        init_nr = int(s[:i + 1])
        if len(str(init_nr)) == len(s):
            break
        x = ""
        counter = 0
        while len(x) <= len(s):
            x += str(init_nr + counter)
            counter += 1
            if x == s:
                break_it = True
                break
        if break_it: break
    if break_it: print("YES " + str(init_nr))
    else: print("NO")
