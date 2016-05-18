#!/usr/bin/env python

from random import randint

lst = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

def perc_up(lst, i):
    if i == 1:
        return
    n = i//2
    if lst[n] > lst[i]:
        lst[n], lst[i] = lst[i], lst[n]
        perc_up(lst, n)

def last_ind(seq):
    return len(seq)-1

def add(lst, val):
    lst.append(val)
    perc_up(lst, last_ind(lst))

def verify(lst, i=1, parent=None):
    if i > last_ind(lst):
        return
    if parent is not None:
        if lst[i] < parent:
            print(i, lst[i], parent)
            raise AssertionError
    verify(lst, i*2, lst[i])
    verify(lst, i*2+1, lst[i])

add(lst, 3)
verify(lst)

def test():
    for _ in range(30):
        lst = [0]
        for _ in range(30):
            add(lst, randint(0,50))
        verify(lst)
    print("verified")
test()


print("lst", lst)
