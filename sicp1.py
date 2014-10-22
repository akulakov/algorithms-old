#!/usr/bin/env python3
import operator

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
# binp(a); binp(b)
# print("out:")
# binp(bitwise_and(a, b))
print()

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

# print(fold([None,None], lambda a,b: [a,b], None))
# print(fold([1], operator.add, 2))
# print(fold([1,2], operator.add, 2))

def last(l):
    """Recursive - get last item in a sequence."""
    if l[1:]:
        return last(l[1:])
    else:
        return l[0]
# print(last([1,3,5,8]))

def A(x, y):
    """Ackerman's function."""
    # print("x,y", x, y)
    if not y: return 0
    if not x: return y*2
    if y==1: return 2
    else:
        y = A(x, y-1)
        return A(x-1, y)

def f(n): return A(2,n)
# for n in range(5): print(n, f(n))

def fib(a, b, count):
    """Fibonacci sequence."""
    if count:
        return fib(a+b, a, count-1)
    else:
        return b

# for n in range(10): print(n, fib(1, 0, n))


# ---- BITFUNC ----------------------------------------------------------------------------------
# p0 exercise
def bitfunc(x):
    return x**4 - 5 * x**2 + 4

def bitfunc_rect(x1, x2):
    # print("bitfunc_rect ", x1, x2)
    return (x2-x1) * bitfunc(x1)

def bitfunc_recur(steps, x1, x2):
    if steps:
        step = (x2-x1) / steps
        return bitfunc_rect(x1, x1+step) + bitfunc_recur(steps-1, x1+step, x2)
    else:
        return 0

def bitfunc_iter(steps, x1, x2):
    step = (x2-x1) / steps
    area = 0
    for n in range(steps):
        area += bitfunc_rect(x1, x1+step)
        x1 += step
        # print("x1", x1)
    return area

def test1():
    bitfunc_recur(950,5,10)

def test2():
    bitfunc_iter(950,5,10)

def compare(*args):
    return abs(bitfunc_recur(*args) - bitfunc_iter(*args))
# print(bitfunc_recur(11, 5, 10))
# print(bitfunc_iter(11, 5, 10))
# print(compare(998, 5, 10))

# ---- COUNT CHANGE -----------------------------------------------------------------------------
def first_denom(n):
    return {1:1, 2:5, 3:10, 4:25, 5:50}[n]

l = [[],[],[]]

def count_change(amount, kinds_of_coins, d=0):
    """Count change algorithm from SICP book."""
    star = '*' if amount==0 else ' '
    if kinds_of_coins:
        l[d].append("%s %d] amount, kinds_of_coins %s %s" % (star, d, amount,kinds_of_coins))
    if amount == 0:
        return 1
    if amount<0 or kinds_of_coins==0:
        return 0
    else:
        amount2 = amount - first_denom(kinds_of_coins)
        # print("amount2", amount2)
        return count_change(amount, kinds_of_coins-1, 1) + \
               count_change(amount2, kinds_of_coins, 2)

# print(count_change(11, 3))
# print(count_change(100, 5))
# for m in l[1]: print(m)
# print()
# for m in l[2]: print(m)

# Exercise 1.11 (page 70)
def f_rec(n):
    if n<3:
        return n
    else:
        return f_rec(n-1) + 2*f_rec(n-2) + 3*f_rec(n-3)

def f_iter(n):
    last = []
    for m in range(n+1):
        if m<3:
            last.append(m)
        else:
            a, b, c = reversed(last)
            last.append(a + 2*b + 3*c)
            del last[0]
    return last[-1]

# print(f_rec(10))
# print(f_iter(10))
# END Exercise 1.11 (page 70)

def p_triangle(l, n):
    """Pascal's triangle."""
    if n==0 or n==l:
        return 1
    return p_triangle(l-1, n-1) + p_triangle(l-1, n)

# print(p_triangle(4, 1))
# print(p_triangle(4, 2))
# print(p_triangle(4, 3))

# Exercise 1.15
def cube(x):
    return x**3

def p(x):
    print("in p()")
    return 3*x - 4*cube(x)

def sine(angle):
    """Exercise 1.15"""
    if abs(angle) <= 0.1:
        return angle
    else:
        return p(sine(angle / 3))
# END Exercise 1.15

def multiply(a, b):
    """Multiply a and b recursively using addition."""
    if b==0: return 0
    else:
        return a + multiply(a, b-1)

def mult2(x, y):
    """ Multiply with doubling / halving,
        aka 'Russian peasant method'; allowed: addition, halving, doubling.
    """
    if y==1:
        return x
    else:
        add = x if y%2 else 0
        return mult2(x*2, y//2) + add

def mult3(x, y):
    """Same as `mult2` but iterative."""
    answer = 0
    while True:
        if y % 2:
            answer += x
        if y < 1:
            break
        x *= 2
        y //= 2
    return answer

# print(sine(12.15))
# print(multiply(3,5))
# print(mult2(9,9))
# print(mult3(9,9))

# Exercise 1.16
def exp():
    """Calc b**n using squaring; using 2**64 here."""
    b   = 2
    n = 64

    # a   = 1
    # print("x", x)
    # x   = a * b**b_n
    # y   = 0
    a   = b**2
    sub = 2
    n -= 2

    while True:
        a **= 2
        n -= sub
        sub *= 2
        if n==0:
            return a

        # y += 1
        # if y>=8: break

        print("a", a)
        # print("b_n", b_n)

        print("sub", sub)
        print("a * b**n", a * b**n)
        print()

print('answer!', exp())
def n(expr):
    print(expr, eval(expr))

if 1:
    n("2**0 * 2**64")
    n("2**1 * 2**63")
    n("2**2 * 2**62")
    n("2**4 * 2**60")
    n("2**8 * 2**56")


# Exercise 1.19
def fib2(n):
    """Fibonacci 2"""
    a,b = 0,1
    lst = [a,b]
    for _ in range(n-2):
        # a, b = b, a + b
        old_a = a
        a = b
        b = old_a + b
        lst.append(b)
    return lst

def fib3(p, q, a, b, n):
    """More general version of Fibonacci with p & q variables."""
    lst = [a, b]
    for _ in range(n-2):
        old_a = a
        a = a*p + b*q   # intead of b
        b = old_a*q + b*q + b*p     # instead of a + b
    return a, b

#
print('-'*70)
# print(fib2(12))
def f_twice():
    a, b = 0, 1
    p, q = 1, 2
    a, b = fib3(p, q, a, b, 4)
    print("a,b", a,b)
    print(fib3(p, q, a, b, 4))

    print(fib3(1,4,0,1,4))

# f_twice()
# END Exercise 1.19

def gcd(a, b):
    """ Calc greatest common divisor.
        With applicative order, modulus is used 6 times, with normal evaluation 7? or also 6????
        Trick question?
        Exercise 1.20
    """
    # substitution: gcd(206, gcd(40, gcd(6, gcd(4, gcd(2, 0)))))
    print("a,b", a,b)
    if not b:
        return a
    else:
        return gcd(b, a % b)

# print(gcd(206, 40))
