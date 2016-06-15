#!/usr/bin/env python3

"""
start: where oldest value was inserted;
    incremented when popping
    sometimes may be incremented when adding, when 'end' pushes start forward
end: where last value was inserted;
    incremented when adding

add:
    end = wrap-increment(end)
    buffer[end] = value
    if end == start:
        wrap-increment(start)

pop:
    return buffer[start]
    wrap-increment(start)

test-add:
    add 3 items
    assert 1,2,3
    add 1 item
    assert 4,2,3

test-pop:
    add 3 items
    assert pop == 1
    assert None, 2, 3
    add items 4, 5
    assert 4, 5, 3
    assert pop() == 3
    assert 4, 5, None

longer example:
[5 6 7 8 9 None None 2 3 4]
"""

class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.buf = [None]*size
        self.end = 0
        self.start = 1

    def wrap_incr(self, val, dir=1):
        return (val+dir) % self.size

    def add(self, val):
        self.end = self.wrap_incr(self.end)
        self.buf[self.end] = val
        if self.start == self.end:
            self.start = self.wrap_incr(self.start)

    def pop(self):
        val = self.buf[self.start]
        if val is not None:
            self.buf[self.start] = None
            self.start = self.wrap_incr(self.start)
            # self.end = self.wrap_decr(self.end)
        return val

    def __str__(self):
        return "S: %s E: %s | %s" %(self.start,self.end,self.buf)


def setup():
    r=RingBuffer(3)
    r.add(1); r.add(2); r.add(3)
    return r

def test_add():
    r=setup()
    assert r.buf == [3,1,2]
    r.add(4)
    assert r.buf == [3,4,2]

def is_eq(a,b):
    if a==b: return 1
    print("Err: val != expected")
    print("val", a)
    print("exp", b)

def test_pop():
    r=setup()
    assert r.pop() == 1
    assert is_eq(r.buf, [3,None,2])

    assert is_eq(r.end, 0)
    r.add(4); r.add(5)
    assert is_eq(r.buf, [3,4,5])
    assert is_eq(r.pop(),3)
    assert is_eq(r.pop(),4)
    assert is_eq(r.buf, [None,None,5])

test_add()
test_pop()

print("All passed..")
