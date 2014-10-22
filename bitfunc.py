#!/usr/bin/env python3

from guppy import hpy
h=hpy()

# ---- BITFUNC ----------------------------------------------------------------------------------
def bitfunc(x):
    return x**4 - 5 * x**2 + 4

def bitfunc_rect(x1, x2):
    # print("bitfunc_rect ", x1, x2)
    return (x2-x1) * bitfunc(x1)

def bitfunc_recur(steps, x1, x2, n=0):
    if steps:
        step = (x2-x1) / steps
        n+=1
        if n==948:
            print h.heap()
        return bitfunc_rect(x1, x1+step) + bitfunc_recur(steps-1, x1+step, x2, n)
    else:
        return 0

def bitfunc_iter(steps, x1, x2):
    step = (x2-x1) / steps
    area = 0
    for n in range(steps):
        area += bitfunc_rect(x1, x1+step)
        x1 += step
        # print("x1", x1)
    return area

def test1():
    print h.heap()
    bitfunc_recur(950,5,10)

def test2():
    bitfunc_iter(950,5,10)

test1()
def compare(*args):
    return abs(bitfunc_recur(*args) - bitfunc_iter(*args))
# print(bitfunc_recur(11, 5, 10))
# print(bitfunc_iter(11, 5, 10))
# print(compare(998, 5, 10))
