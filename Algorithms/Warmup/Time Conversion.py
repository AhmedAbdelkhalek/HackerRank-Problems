#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/time-conversion/problem

# accept the time as string
time = input().strip()
# first ignore AM/PM and store time in variables.
h, m, s = map(int, time[:-2].split(':'))
# the last to letters stored in this variable.
p = time[-2:]

# (p.upper() == 'PM') * 12 is meant to add 12 hours if time after 12 PM to be displayed in 24h format.
h = h % 12 + (p.upper() == 'PM') * 12
# print the time in 00:00:00 format
print(('%02d:%02d:%02d') % (h, m, s))
