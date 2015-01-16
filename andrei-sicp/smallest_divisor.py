#!/usr/bin/env python3
import operator
p = print

def prime(x):
    for a in range(2, x):
        if a**2 > x:
            return True
        elif (x % a) == 0:
            # print("a", a)
            return False
    return True

for x in range(2, 100):
    if prime(x):
        pass
        # print(x)

# print("prime(199)", prime(199))
# print("prime(1999)", prime(1999))
# print("prime(19999)", prime(19999))

import itertools
def smallest_divisor(x):
    for a in range(2, x):
    # for a in itertools.chain( [2], range(3, x, 2) ):
        if a**2 > x:
            return x
        elif (x % a) == 0:
            # print("a", a)
            return a

def t1():
    smallest_divisor(1999)

for x in (199,1999,19999):
    print(smallest_divisor(x))
