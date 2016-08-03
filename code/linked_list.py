#!/usr/bin/env python3

from time import sleep

class LinkedList:
    def __init__(self):
        self.first = self.last = None

    def add(self, val):
        node = [val, None]
        if self.last:
            self.last[1] = self.last = node
        else:
            self.first = self.last = node

    def __iter__(self):
        item = self.first
        while item[1]:
            yield item[0]
            item = item[1]
        yield item[0]


l=LinkedList()
for x in range(10):
    l.add(x)
print("list(l)", list(l))

def reverse_list(ll):
    last = None
    cur = orig_first = ll.first
    while cur:
        next = cur[1]
        if last:
            cur[1] = last
        last = cur
        cur = next
        sleep(0.1)
    orig_first[1] = None
    ll.first = last

reverse_list(l)
print("list(l)", list(l))
