#!/usr/bin/env python3

def A(x, y):
    """#1.10 Ackermann's function."""
    # print("x,y", x, y)
    if not y: return 0
    if not x: return y*2
    if y==1: return 2
    else:
        y = A(x, y-1)
        return A(x-1, y)

# 2^65536  2^2^65536
print("ackermann", A(4,3))
def f(n):
    return A(2,n)
for n in range(5):
    print(n, f(n))
