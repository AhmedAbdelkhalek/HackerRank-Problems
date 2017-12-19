#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""


# only in python2
def insert(r, val):
    # Enter you code here.
    if r is None:
        r = Node(val)
    elif val < r.data:  # left branch
        if r.left is None:
            r.left = Node(val)
        else:
            insert(r.left, val)
    elif val > r.data:  # right branch
        if r.right is None:
            r.right = Node(val)
        else:
            insert(r.right, val)
    return r
