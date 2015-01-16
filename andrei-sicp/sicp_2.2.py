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


# 2.25
def ex2_25():
    l = lisplist([1, 3, [5, 7], 9])
    print("l", l)
    print(car(cdr(car(cdr(cdr(l))))))
    div()

    l = lisplist([[7]])
    p(l)
    p(car(car(l)))

    l = lisplist( (1, (2, (3, (4, (5, (6, 7)))))) )
    p(l)
    p(car(cdr(car(cdr(car(cdr(car(cdr(car(cdr(car(cdr(l)))))))))))))

ex2_25()
# p(count_leaves(l))
