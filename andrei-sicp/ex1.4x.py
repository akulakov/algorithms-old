#!/usr/bin/env python3
import operator
p = print

def inc(x):
    return x+1

def cubic(a, b, c):
    """1.40"""
    def inner(x):
        return x**3 + a*x**2 + b*x + c
    return inner

def double(f):
    """1.41: Apply `f` two times."""
    def inner(x):
        return f(f(x))
    return inner

from functools import reduce
def compose(*functions):
    """1.42"""
    def inner(x):
        # shorter but less readable alternative
        # return reduce(lambda x, y: y(x), reversed(functions), x)
        for f in reversed(functions):
            x = f(x)
        return x
    return inner

def repeated(f, n):
    """1.43: Repeatedly apply `f` function `n` times."""
    return compose(*[f]*n)

def square(x):
    return x**2

def smooth(f, dx=1):
    """1.44"""
    def inner(x):
        return (f(x-dx) + f(x) + f(x+dx)) / 3
    return inner

def avg(a, b):
    return (a+b) / 2

def avg_damp(f):
    def inner(x):
        return avg(x, f(x))
    return inner

def over1k(x): return x > 1000
def dbl(x): return x*2

def iter_improve(good_enough, improve):
    """1.46"""
    def inner(x):
        while not good_enough(x):
            x = improve(x)
        return x
    return inner

dbl_inc = double(double(double(inc)))
sqr_inc = compose(square, inc)
sqr_5 = repeated(square, 5)
# print("sqr_5(2)", sqr_5(2))
# print(repeated(square, 2)(5))
# print("dbl_inc(5)", dbl_inc(5))
# print("sqr_inc(5)", sqr_inc(5))
# print("smooth(square, 1)(25)", smooth(square, 1)(25))
x = repeated(smooth, 5)(square)(25)
# print("x", x)

f = iter_improve(over1k, dbl)
x = f(2)
# print("x", x)
