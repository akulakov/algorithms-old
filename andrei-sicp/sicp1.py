#!/usr/bin/env python3
import operator
p = print

def append(a, b):
    if not a:
        return b
    else:
        first, rest = a
        return cons(first, append(rest, b))

def last(l):
    """Recursive - get last item in a sequence."""
    if l[1:]:
        return last(l[1:])
    else:
        return l[0]

def lisplist(lst):
    if lst:
        a, *b = lst
    else:
        return None
    return [a, lisplist(b)]

def lispmap(func, lists):
    # page 146, lisp style map!
    return (func(x) for x in zip(*lists))

def square_list(items):
    def iter(things, answer):
        if not things:
            return answer
        else:
            c = cons(square(car(things)), answer)
            print("c", c)
            return iter(cdr(things), c)
    return iter(items, None)

print(square_list([3,5,8,9,10]))

# print(last([1,3,5,8]))

# p(lisplist(range(10)))
# print(append(lisplist([1,2,3]), lisplist([11,12,15])))
