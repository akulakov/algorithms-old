#!/usr/bin/env python3
import operator
p = print

def cube(x):
    return x**3

def p2(x):
    print("in p2()")
    return 3*x - 4*cube(x)

def sine(angle):
    """Exercise 1.15"""
    if abs(angle) <= 0.1:
        return angle
    else:
        return p(sine(angle / 3))
print(sine(12.15))
