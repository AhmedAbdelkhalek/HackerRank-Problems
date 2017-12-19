#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


# only in python2
def preOrder(root):
    if root:
        print(str(root.data)),  # stupid python2 comma at the end
        preOrder(root.left)
        preOrder(root.right)
