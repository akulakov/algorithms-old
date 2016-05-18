#!/usr/bin/env python3

def binp(x):
    """Print out `x` in binary format."""
    print("{:3} {:08b}".format(x, x))

def bitwise_and(a, b):
    result = 0
    mask = 1
    while a and b:
        if (a % 2) == (b % 2) == 1:
            result += mask
        mask <<= 1
        a >>= 1
        b >>= 1
    return result

a, b = 101, 115
binp(a); binp(b)
print("out:")
binp(bitwise_and(a, b))
