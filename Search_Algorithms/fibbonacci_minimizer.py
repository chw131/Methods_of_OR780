#!/usr/bin/env python
# -*- coding: utf-8 -*-

#fibonacci numbers
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def func(x):
	return x**4 - 14*x**3 + 60*x**2 - 70*x

#List fibonacci
# st: list
#  u: fibnacci n
#  s: start idex
#  l: list size
#key: search key
def fib_search(n,f,a,b, x1, x2,tol):
    if n <= 4:
        return -1
    

    if (f(x1) < f(x2)):
    	a = x1
    	x1 = x2
    	x2= a + fib(n-2)/fib(n)*(b-a)
    else:
        b = x2
        x2 = x1
        x1 = a + fib(n-1)/fib(n)*b

    print (n, a, b, x1, x2)
    return fib_search(f,a,b,x1,x2,tol)

#main
if __name__ == '__main__':
	tol = 0.1
    arr = [5,8,13,19,21,37,56,64,75,80,88]
    a = 0.0
    b = 2.0
    n = 10
    # initialize x1, x2
    x1 = a + fib(n-2)/fib(n)*(b-a)
    x2 = a + fib(n-)/fib(n)*b
    fib_search(n,func, a, b, x1, x2, tol)    

   

 #   for key in arr:
 #       print ("search key %d, idx: %d" % (key, fib_search(arr, u, 0, len(arr), key)))

 #   for key in [100,20,32,12]:
 #       print ("search key %d, idx: %d" % (key, fib_search(arr, u, 0, len(arr), key)))
 