#!/usr/bin/env python3


class LinkedList:
    def __init__(self):
        self.last = None

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
