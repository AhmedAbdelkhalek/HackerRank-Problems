#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.

for i in range( int(n//2)):

    print( ( '.|.'*(2*(i+1)-1)).center(m,'-') )
print( 'WELCOME'.center(m,'-'))
for i in range (int(n//2)-1,-1,-1):
    print(( '.|.'*(2*(i+1)-1)).center(m, '-'))


