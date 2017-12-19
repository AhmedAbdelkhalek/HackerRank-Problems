#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/equal-stacks/problem

import sys


class Stack:
    def __init__(self):
        self.items = []
        self.stackSum = 0

    def push(self, data):
        self.items.append(data)
        self.stackSum += data

    def pop(self):
        poped = self.items.pop()
        self.stackSum -= poped
        return poped

    def max(self):
        return max(self.items)

    def peek(self):
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def height(self):
        return self.stackSum


n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
# create three blank stacks.
s1 = Stack()
s2 = Stack()
s3 = Stack()
# they input is reversed, so we reverse it again. and push to stack directly.
[s1.push(int(h1_temp)) for h1_temp in reversed(input().strip().split(' '))]
[s2.push(int(h2_temp)) for h2_temp in reversed(input().strip().split(' '))]
[s3.push(int(h3_temp)) for h3_temp in reversed(input().strip().split(' '))]

# Stat the process till it meats the equal stacks condition.
while True:
    # if equality is found then print the height and go out.
    # note, the condition should be here instead of ### position
    # that is because, some stacks entered are already equal.
    if s1.height() == s2.height() == s3.height():
        print(s1.height())
        break

    # get out if all stacks are empty.
    if s1 is None and s2 is None and s3 is None:
        print(0)

    # check the tallest stack and pop 1 node of it.
    tallest = max(s1.height(), s2.height(), s3.height())
    tallestIndex = [s1.height(), s2.height(), s3.height()].index(tallest)
    tallestStack = [s1, s2, s3][tallestIndex]
    tallestStack.pop()
    ###
