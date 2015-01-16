#!/usr/bin/env python3
import operator
p = print

# Exercise 1.11 (page 70)
def f_rec(n):
    if n<3:
        return n
    else:
        return f_rec(n-1) + 2*f_rec(n-2) + 3*f_rec(n-3)

def f_iter(n):
    last = []
    for m in range(n+1):
        if m<3:
            last.append(m)
        else:
            a, b, c = reversed(last)
            last.append(a + 2*b + 3*c)
            del last[0]
    return last[-1]

print(f_rec(10))
print(f_iter(10))
