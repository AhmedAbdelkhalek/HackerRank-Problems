#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re
txt = input()
ptr = re.compile(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]*[AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]")
v=ptr.findall(txt)
#print(v)
if v == [] :
    print(-1)
for i in v:
    ptr2= re.compile("[AEIOUaeiou]{2,}")
    x = ptr2.findall(i)
    print(x[0])
