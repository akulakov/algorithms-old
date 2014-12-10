#!/usr/bin/env python3
import operator
p = print

"""
(define (count-leaves x)
      (cond ((null? x) 0)
            ((not (pair? x)) 1)
            (else (+ (count-leaves (car x))
                     (count-leaves (cdr x))))))
"""

def car(lst):
    return lst[0]
def cdr(lst):
    return lst[1:]
def cons(a, b):
    return a, b
def is_pair(x):
    return hasattr(x, "__getitem__")
def lisplist(lst):
    if lst:
        a, *b = lst
    else:
        return None
    return [a, lisplist(b)]

def count_leaves(x):
    # 2.24
    if not x:
        return 0
    elif not is_pair(x):
        return 1
    else:
        return count_leaves(car(x)) + count_leaves(cdr(x))

l = lisplist([1,3,8,22,21,27])
p(count_leaves(l))
