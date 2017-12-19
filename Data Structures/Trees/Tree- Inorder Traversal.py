#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/tree-inorder-traversal/problem


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


# only in python2
def inOrder(root):
    # Write your code here
    if root:
        inOrder(root.left)
        print(str(root.data)),  # stupid python2 comma at the end
        inOrder(root.right)
