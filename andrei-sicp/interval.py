#!/usr/bin/env python3
import operator
p = print

class Interval:
    def __init__(self, a=None, b=None):
        self.a, self.b = a, b   # lower and upper bounds

    def _init_center_width(self, c, w):
        self.a, self.b = c-w, c+w

    def _init_center_width_perc(self, c, perc):
        perc /= 100
        self.a, self.b = c-c*perc, c+c*perc

    def __repr__(self):
        return "%.2f-%.2f" % (self.a, self.b)

    def __add__(self, i):
        return Interval(self.a+i.a, self.b+i.b)

    def __sub__(self, i):
        """#2.8"""
        return Interval(self.a-i.a, self.b-i.b)

    def __mul__(self, i):
        s = self
        tup = s.a*i.a, s.a*i.b, s.b*i.a, s.b*i.b
        return Interval(min(tup), max(tup))

    def __truediv__(self, i):
        if not i.b or not i.a:
            raise ZeroDivisionError("Cannot divide be a zero-bound interval")
        return self * Interval(1/i.b, 1/i.a)

    def __rtruediv__(self, o):
        return Interval(o/self.a, o/self.b)

    @property
    def percent(self):
        # 2.12
        return 100 * self.width / self.center

    @property
    def center(self):
        # 2.12
        return self.a + self.width

    @property
    def width(self):
        return (self.b-self.a) / 2

i = Interval()
i._init_center_width_perc(10, 50)
print("i", i)
print("i.percent", i.percent)

# #2.9
# let x and y be intervals, z = x+y; a and b are lower and upper bounds
# x.width = (x.b - x.a) / 2
# z.width = (x.b+y.b - x.a+y.a) / 2

def f(a,b,c,d):
    i1, i2 = Interval(a,b), Interval(c,d)
    print("1/i1", 1/i1)
    print("i1,i2", i1,i2)
    print("i1.percent", i1.percent)
    print("i2.percent", i2.percent)
    print("(i1*i2).percent", (i1*i2).percent)
    # print("i1*i2", i1*i2)
    print("(i1*i2)/(i1+i2)", (i1*i2)/(i1+i2))
    print("2nd: ", 1/(1/i1 + 1/i2))
f(5,6,7,8)
