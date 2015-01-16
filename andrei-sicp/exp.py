#!/usr/bin/env python3

# Exercise 1.16
def exp(b, n):
    """ Calc b**n using only squaring operation.

        `n` needs to be an integer because otherwise we would need to use raise to `m` operation where
        `m` != 2, or an equivalent operation, which is not allowed in this task.
    """
    if n==0: return 1
    a   = b
    a_n = 1

    while True:
        last_an = a_n
        a_n *= 2
        b_n = n - a_n

        if b_n == 0:
            return a**2
        elif b_n < 0:
            # if cannot use squaring anymore, go the rest of way by repeated multiplication by `b`
            for _ in range(n-last_an):
               a *= b
            return a
        a **= 2

class State:
    a_n, a = 0, 1
    def __init__(self, b, n):
        self.b = b
        self.n = n
        self.a = 1
        self.a_n = 0

    def __repr__(self):
        return "self.a_n = %s, self.a = %s, self.b_n = %s" % (self.a_n,self.a, self.b_n)

    def step(self):
        """ We need special handling of the initial step.

            If we could use 'raise to power' operation, we could use `a_n` to calculate all values of
            `a`, starting with 0:
            a = b**0 => 1
            a = b**1 => b
            a = b**2 => ..

            But as we can not, we have to special-case the step where `a` advances from 1 to b.
        """
        if self.a_n:
            self.a_n *= 2
            self.a **= 2
        else:
            self.a_n = 1
            self.a = self.b

    @property
    def b_n(self):
        return self.n - self.a_n

    @property
    def next_b_n(self):
        return self.n - self.a_n*2

# Exercise 1.16
def exp(b, n):
    s = State(b, n)

    while True:
        if s.b_n == 0:
            return s.a
        elif s.next_b_n < 0:
            # cannot use squaring anymore, go the rest of way by repeated multiplication
            for _ in range(s.b_n):
               s.a *= s.b
            return s.a
        s.step()

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
