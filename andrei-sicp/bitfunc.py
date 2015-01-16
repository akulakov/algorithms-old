#!/usr/bin/env python3

from math import sqrt
import operator
# from guppy import hpy
# h=hpy()

# ---- BITFUNC ----------------------------------------------------------------------------------
def bitfunc(x):
    return x**4 - 5 * x**2 + 4

def bitfunc_rect(x1, x2):
    # print("bitfunc_rect ", x1, x2)
    return rect(x1, x2, bitfunc(x1), bitfunc(x2))

def rect(x1, x2, y1, y2):
    # note: y2 is f(x2), so not used here
    return (x2-x1) * y1

def trapezoid(x1, x2, y1, y2):
    return (1/2) * (x2-x1) * (y2+y1)

def circle_func(x):
    try:
        return 4 * sqrt(1 - x**2)
    except Exception as e:
        return 0

def circle_rect(x1, x2):
    """P1.2"""
    return rect(x1, x2, circle_func(x1), circle_func(x2))

def func_piece(piece, f, x1, x2):
    """Calc area slice under function `f`, x1->x2, using shape calculated with `piece`."""
    return piece(x1, x2, f(x1), f(x2))

def bitfunc_recur(steps, x1, x2, n=0):
    if steps:
        step = (x2-x1) / steps
        return bitfunc_rect(x1, x1+step) + bitfunc_recur(steps-1, x1+step, x2, n)
    else:
        return 0

def integral_with(piece, func, steps, x1, x2):
    """p1.3"""
    step = (x2-x1) / steps
    area = 0
    for n in range(steps):
        area += func_piece(piece, func, x1, x1+step)
        x1 += step
        # print("x1", x1)
    return area

def bitfunc_iter(*args):
    return integral_with(rect, bitfunc, *args)

def test1():
    bitfunc_recur(950,5,10)

def test2():
    bitfunc_iter(950,5,10)

test1()
def compare(*args):
    return abs(bitfunc_recur(*args) - bitfunc_iter(*args))

sentinel = object()
def fold(l, op, init_val=sentinel):
    """Generic fold operation."""
    if not l:
        return init_val
    if init_val is not sentinel:
        return op(init_val, fold(l, op))
    elif l[1:]:
        first, *rest = l
        return op(first, fold(rest, op))
    else:
        return l[0]

# print(fold([2,3,4], operator.mul))

def to_num(a, default=None):
    try:
        return float(a)
    except:
        try:
            return eval(a)
        except:
            return default

def r(x):
    return repr(x)

class Deriv:
    """p1.7, p1.8"""
    def __init__(self, wrt):
        self.wrt = wrt

    def add(self, *args):
        return sum( [self.deriv(a) for a in args] )

    def mult_ab(self, a, b=None):
        return to_num(a) * self.deriv(b) + to_num(b) * self.deriv(a)

    def mult(self, *args):
        return fold(args, self.mult_ab)

    def deriv(self, expr):
        ops = {'+': self.add, '*': self.mult}
        val = to_num(expr)

        if val is None and ' ' in expr:
            op, *args = expr.split()
            if op in ops:
                return ops[op](*args)
        elif expr == self.wrt:
            return 1
        elif val is not None:
            return 0
        else:
            return 0

def test():
    # p1.9
    assert Deriv('y').deriv('y') == 1
    assert Deriv('x').deriv('y') == 0
    assert Deriv('x').deriv('5') == 0
    assert Deriv('x').deriv('+ x 3 6 x 7 x') == 3
    assert Deriv('x').deriv('* x x 4') == 4
    print("All test pass..")


### P1

# p1.4
# print("P1.2", integral_with(trapezoid, circle_func, 5000, 0, 1))

# p1.7
x = 5
# print("P1.7  + x 3 =", Deriv('x').deriv("+ x 3 6 x 7 x"))
print("P1.7  * x 2 =", Deriv('x').deriv("* x 1"))
test()

# print(bitfunc_recur(11, 5, 10))
# print(bitfunc_iter(11, 5, 10))
# print(compare(998, 5, 10))
