#!/usr/bin/env python3
import operator
p = print

def p_triangle(l, n):
    """#1.12 Pascal's triangle."""
    if n==0 or n==l:
        return 1
    return p_triangle(l-1, n-1) + p_triangle(l-1, n)

print(p_triangle(4, 1))
print(p_triangle(4, 2))
print(p_triangle(4, 3))
