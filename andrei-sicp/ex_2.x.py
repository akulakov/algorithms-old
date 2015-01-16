#!/usr/bin/env python3
import operator
p = print

### 2.x

def make_rat(a, b):
    """2.1"""
    sign = (a<0 and b<0) or (a>=0 and b>=0)
    sign = '' if sign else '-'
    x = gcd(a, b)
    return "%s%d/%d" % (sign, abs(a/x), abs(b/x))


class Rect:
    """#2.3"""
    def __init__(self, p1, p2):
        # upper left, lower right
        self.points = p1, p2

    @property
    def sides(self):
        p1, p2 = self.points
        return p2[0]-p1[0], p2[1]-p1[1]

    def perim(self):
        return self.sides[0]*2 + self.sides[1]*2

    def area(self):
        return self.sides[0] * self.sides[1]

def cons(x, y):
    """#2.4"""
    return lambda f: f(x, y)
def car(z):
    return z(lambda p,q: p)
def cdr(z):
    return z(lambda p,q: q)

def car(lst):
    return lst[0]
def cdr(lst):
    return lst[1:]
def cons(a, b):
    return a, b

class A:
    def attr_a(self, arg=sentinel):
        """Get or set attr."""
        if arg==sentinel:
            return self.a
        else:
            self.a = arg
