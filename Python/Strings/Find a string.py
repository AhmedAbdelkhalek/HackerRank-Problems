#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    j=0
    for i in range(len(string)-len(sub_string)+1):
        #print(string[i:i+len(sub_string)])
        if sub_string == string[i:i+len(sub_string)]:
            j+=1
    return(j)

x = input()
y = input()
print(count_substring(x,y))
