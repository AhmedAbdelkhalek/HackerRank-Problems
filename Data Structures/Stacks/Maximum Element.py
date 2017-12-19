#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/maximum-element/problem

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class Stack:
    # Start the stack, set the top to nothing and the size = 0
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self,newData):
        # Top
        # Next
        # Next
        newNode = Node(newData)
        if self.top is None:
            self.top = newNode
            self._size = 1
        else:
            newNode.next = self.top
            self.top = newNode
            self._size += 1
    def pop(self):
        if self.top:
            data = self.top.data
            self._size -= 1
            if self.top.next:
                self.top = self.top.next
                return data
            else:
                self.top = None
                return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def __len__(self):
        return self._size

    def __iter__(self):
        if self.top is None:
            yield None
        else:
            cur = self.top
            while cur:
                val = cur
                cur = cur.next
                yield val


    def max(self):
        max_value = -9^10
        for v in self.__iter__():
            if v.data > max_value:
                max_value = v.data
        return max_value


s = Stack()
maxes = Stack()
nrOfLines = int(input())
for i in range(nrOfLines):
    line = input().split(" ")
    oper = int(line[0])

    if oper == 1:
        val = int(line[1])
        s.push(val)
        if len(s) == 1 or val >=  maxes.peek() :
            maxes.push(val)
    elif oper == 2:
        poped = s.pop()
        if poped == maxes.peek():
            maxes.pop()
    elif oper == 3:
        print(maxes.peek())


