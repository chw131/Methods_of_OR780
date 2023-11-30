#!/usr/bin/env python
# -*- coding: utf-8 -*-

#fibonacci numbers
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#List fibonacci
# st: list
#  u: fibnacci n
#  s: start idex
#  l: list size
#key: search key
def fib_search(st,u, s, l, key):
    if u < 1:
        return -1
    idx = s + fib(u-1) -1

    if idx < l:
        if key == st[idx]:
            return idx
        elif key > st[idx]:
            s = idx + 1
    return fib_search(st,u-1, s, l, key)

#main
if __name__ == '__main__':
    arr = [5,8,13,19,21,37,56,64,75,80,88]

    print ("idx", "item")
    for i, v in enumerate(arr):
        print (i, v)

    u = 0
    while fib(u) < len(arr):
        u += 1

    for key in arr:
        print ("search key %d, idx: %d" % (key, fib_search(arr, u, 0, len(arr), key)))

    for key in [100,20,32,12]:
        print ("search key %d, idx: %d" % (key, fib_search(arr, u, 0, len(arr), key)))
 