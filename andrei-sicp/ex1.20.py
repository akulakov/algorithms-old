#!/usr/bin/env python3
import operator
p = print

def gcd(a, b):
    """ #1.20 Calc greatest common divisor.
        With applicative order, modulus is used 6 times, with normal evaluation 7? or also 6????
        Trick question?
    """
    # substitution: gcd(206, gcd(40, gcd(6, gcd(4, gcd(2, 0)))))
    # print("a,b", a,b)
    if not b:
        return a
    else:
        return gcd(b, a % b)

print(gcd(206, 40))
