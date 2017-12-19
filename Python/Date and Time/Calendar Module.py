#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/calendar-module/problem

import datetime
n = (input())
#n ="8 5 2015"
i = n.split(' ')

j = datetime.date(int(i[2]),int(i[0]),int(i[1]))
print(j.strftime("%A").upper())