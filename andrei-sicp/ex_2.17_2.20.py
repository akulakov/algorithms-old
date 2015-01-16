#!/usr/bin/env python3
import operator
p = print

def last_pair(lst):
    # 2.17
    if lst[1] is None:
        return lst
    else:
        return last_pair(lst[1])

def same_parity(*args):
    # 2.20
    assert args
    return [a for a in args if a%2 == args[0]%2]
