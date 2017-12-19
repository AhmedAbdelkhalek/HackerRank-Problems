#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# for this code, we create the upper right corner any way we want
# then make a first mirror (Horizontal mirror)
# then make a vertical mirror

# note that the mirror avoid the axis.
def print_rangoli(size):
    sq = size * 2 - 1
    v = upper_right(size, sq)
    #v = '*-*-\n----\n*5*5'         'You can test this
    d = h_mirror(v)
    print(d)
    f = v_mirror(d)
    print(f)


def upper_right(size, sq):
    y = []
    for i in range(size - 1, -1, -1):
        y.append('-'.join(x[i:size]).ljust(sq, '-'))
    return '\n'.join(y)


def h_mirror(the_str):
    t = the_str.split('\n')
    b = []
    for i in t:
        b.append(''.join(reversed(i[1:])) + i)
    return '\n'.join(b)


def v_mirror(the_str):
    t = the_str.split('\n')
    b = []
    for i in t[0:len(t) - 1]:
        b.insert(0, i)
    return ('\n'.join(b))


x = []
for i in range(97, 97 + 26):
    x.append(chr(i))

o = int(input())
print_rangoli(o)


