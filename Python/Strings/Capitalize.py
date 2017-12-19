#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/capitalize/problem

def capitalize(string):
    return (' '.join([i.capitalize() for i in string.split(" ")]))

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)