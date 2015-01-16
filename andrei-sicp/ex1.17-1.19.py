#!/usr/bin/env python3
import operator
p = print

def multiply(a, b):
    """#1.17 Multiply a and b recursively using addition."""
    if b==0: return 0
    else:
        return a + multiply(a, b-1)

def mult2(x, y):
    """ #1.18 Multiply with doubling / halving,
        aka 'Russian peasant method'; allowed: addition, halving, doubling.
    """
    if y==1:
        return x
    else:
        add = x if y%2 else 0
        return mult2(x*2, y//2) + add

def mult3(x, y):
    """#1.18 Same as `mult2` but iterative."""
    answer = 0
    while True:
        if y % 2:
            answer += x
        if y < 1:
            break
        x *= 2
        y //= 2
    return answer

print(multiply(3,5))
print(mult2(9,9))
print(mult3(9,9))


# EXERCISE 1.16
# exp() -- moved to exp.py

def fib2(n):
    """#1.19 NOT WORKING! Fibonacci 2"""
    a,b = 0,1
    lst = [a,b]
    for _ in range(n-2):
        # a, b = b, a + b
        old_a = a
        a = b
        b = old_a + b
        lst.append(b)
    return lst

def fib3(p, q, a, b, n):
    """More general version of Fibonacci with p & q variables."""
    lst = [a, b]
    for _ in range(n-2):
        old_a = a
        a = a*p + b*q   # intead of b
        b = old_a*q + b*q + b*p     # instead of a + b
    return a, b

#
print('-'*70)
print(fib2(12))
def f_twice():
    a, b = 0, 1
    p, q = 0, 1
    a, b = fib3(10, 20, 0, 1, 4)

    print(fib2(4))
    print("a,b", a,b)
    # a, b = fib3(p, q, a, b, 4)
    # print(fib3(p, q, a, b, 4))

    # print(fib3(1,4,0,1,4))

f_twice()
