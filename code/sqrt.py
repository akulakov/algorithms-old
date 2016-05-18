#!/usr/bin/env python

def average(x, y):
    return (x+y)/2

def sqrt(x, guess=1):
    def improve_guess(g):
        return average(x/g, g)

    def good_enough(new):
        return abs(new**2 - x) <= 0.000001

    new = improve_guess(guess)
    if good_enough(new):
        return new
    else:
        return sqrt(x, new)

print(sqrt(2))
