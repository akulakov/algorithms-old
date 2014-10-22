#!/usr/bin/env python3

# Exercise 1.16
def exp(b, n):
    """Calc b**n using only squaring operation."""
    a   = b
    a_n = 1
    while True:
        a **= 2
        a_n *= 2
        if (n-a_n)==0:
            return a
        # if y>=8: break

        print("a", a)
        print("a_n", a_n)
        print("a * b ** (n-a_n)", a * b**(n-a_n))
        print()

# print('answer!  ', exp(5, 32), '\n')
print('answer!  ', exp(5, 64), '\n')

def n(expr):
    print(expr, '==', eval(expr))
n("5**64")

if 0:
    n("2**0 * 2**64")
    n("2**1 * 2**63")
    n("2**2 * 2**62")
    n("2**4 * 2**60")
    n("2**8 * 2**56")
