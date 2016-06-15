#!/usr/bin/env python3

class Alist:
    "Association list."
    def __init__(self):
        self.last = self.first = []

    def add(self, key, val):
        node = [key, val, None]
        if self.last:
            self.last[2] = node
            self.last = node
        else:
            self.first = self.last = node

    def __iter__(self):
        item = self.first
        while item[2]:
            yield item[:2]
            item = item[2]
        yield item[:2]

    def __getitem__(self, key):
        for k,v in self:
            if k==key:
                return v
        raise KeyError

    def get(self, key, default=None):
        try: return self[key]
        except KeyError: return default

lst = Alist()
lst.add('a', 1)
lst.add('b', 2)
print("lst.first", lst.first)
print("list(lst)", list(lst))
print("lst['a']", lst['a'])
print("lst['b']", lst['b'])
print("lst.get('c')", lst.get('c'))
print("lst['c']", lst['c'])
