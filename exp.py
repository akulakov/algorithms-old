#!/usr/bin/env python3

# Exercise 1.16
def exp(b, n):
    """ Calc b**n using only squaring operation.

        `n` needs to be an integer because otherwise we would need to use raise to `m` operation where
        `m` != 2, or an equivalent operation, which is not allowed in this task.
    """
    if n==0: return 1
    a   = b
    a_n = next_n = 1

    while True:
        next_n *= 2

        # if cannot use squaring anymore, go the rest of way by repeated multiplication by `b`
        if (n-next_n) < 0:
            for _ in range(n-a_n):
               a *= b
            return a
        else:
            a_n = next_n

        a **= 2
        if (n-a_n) == 0:
            return a

# print('answer!  ', exp(5, 32), '\n')
b, n = 2, 69
print('answer:', exp(b, n), '\n')

def f(expr):
    print(expr, '==', eval(expr))
f("%s**%s" % (b, n))

if 0:
    f("2**0 * 2**64")
    f("2**1 * 2**63")
    f("2**2 * 2**62")
    f("2**4 * 2**60")
    f("2**8 * 2**56")
