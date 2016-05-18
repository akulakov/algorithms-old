#!/usr/bin/env python3
import operator

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

print(fold([None,None], lambda a,b: [a,b], None))
print(fold([1], operator.add, 2))
print(fold([1,2], operator.add, 2))
