#!/usr/bin/env python3

# Exercise 1.16
def exp(b, n):
    a   = b
    sub = 1
    while True:
        a **= 2
        sub *= 2
        if (n-sub)==0:
            return a
        # if y>=8: break

        print("a", a)
        print("sub", sub)
        print("a * b ** (n-sub)", a * b**(n-sub))
        print()

def exp2(b, n):
    a   = b
    a_n = 1
    while True:
        a_n *= 2
        if (n-a_n)==0:
            return a**a_n

        print("a_n", a_n)
        print(a**a_n * b ** (n-a_n))
        print()

# print('answer!  ', exp(5, 32), '\n')
print('answer!  ', exp2(5, 32), '\n')
print("2**32 =", 5**32)

def n(expr):
    print(expr, eval(expr))

if 0:
    n("2**0 * 2**64")
    n("2**1 * 2**63")
    n("2**2 * 2**62")
    n("2**4 * 2**60")
    n("2**8 * 2**56")
