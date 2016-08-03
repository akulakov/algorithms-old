#!/usr/bin/env python3
import operator
p = print


def div(): p( '-'*10, '\n')
def car(lst):
    return lst[0]
def cdr(lst):
    return lst[1]
def cons(a, b):
    return a, b
def is_pair(x):
    return hasattr(x, "__getitem__")
def lisplist(lst):
    if lst:
        a, *b = lst
        if hasattr(a, "__getitem__"):
            a = lisplist(a)
    else:
        return None
    return [a, lisplist(b)]

def count_leaves(x):
    if not x:
        return 0
    elif not is_pair(x):
        return 1
    else:
        return count_leaves(car(x)) + count_leaves(cdr(x))

def square(x):
    return x**2
