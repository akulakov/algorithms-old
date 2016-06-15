#!/usr/bin/env python3

""" Skip list

- implemented with a list of pointers for each node instead of linked list at
each level.

TODO:
1. add unit tests
2. add node.__bool__ always returing True, avoids many checks for 'is None', 'is not None'
3. separate LinkedList is probably not needed? Only for testing?
4. has_real_pointers rename to has_pointers, don't need to check for None pointers at all.
"""

from random import random
from skip_list_lib import *

class SkipList:
    def __init__(self):
        self.ll = LinkedList()
        self.max = 0
        self.first = None
        self.def_n = 0  # override `n` if set

    def __iter__(self, level=0):
        item = self.first
        while item and item.has_real_pointers():
            yield item
            item = item[level]
        if item is not None:
            yield item

    def update_max(self, h):
        "Update max height and first node pointers - first node should have max # of levels."
        if h>self.max:
            self.first.extend([None] * (h-len(self.first)))
            self.max = h

    def add(self, val):
        if self.first is None:
            self.first = Node(val)
            return
        item = last = self.first
        i = len(item)-1
        last_lst = [Item(item, i)]

        # find the location to add node, create and add it
        while 1:
            # backtrack because we ran into a larger value item
            if item>val:
                if i==0:
                    # lowest level, add node before current
                    item = last
                    n = Node(val, item[0])
                    item[0] = n
                    item = n
                    break
                else:
                    # backtrack and search at lower level
                    i-=1
                    item = last
                    continue
            last = item
            last_lst.append(Item(item, i))

            # if last item is less than value, add new node at the end
            if not item.has_real_pointers() and val>item:
                n = Node(val)
                try: item[0] = n
                except IndexError: item.add(n)

                # add all pointers to last_lst because they will all need to be updated
                for i in range(i-1,0,-1):
                    last_lst.append(Item(item, i))
                item = n
                break

            # go to next item OR decrease level
            item2 = getitem(item, i)
            if item2 is not None:
                item = item2
            else:
                i-=1

        # calc num of levels for new node & create pointers accordingly
        n = 1
        while random()<.25:
            n += 1
        n = self.def_n or n     # override for testing
        self.update_max(n)
        item.extend( [None] * (n-len(item)) )

        for x in range(1,n):
            ll = [i for i in last_lst if i.level==x]
            if ll:
                last = ll.pop()
                if last.pointer is None and ll:
                    prev = ll.pop()
                    prev.set_pointer(last.node)
                elif last.pointer is not None:
                    item[last.level] = last.pointer
                last.set_pointer(item)

    def find(self, val):
        item = last = self.first
        i = len(item.pointers)-1

        while 1:
            if item.val==val:
                return item
            if i<=0 and not item.pointers:
                break
            if item>val:
                i-=1
                item = last
                continue
            last = item

            try:
                item = item[i]
            except IndexError:
                # set `i` to the "top" (farthest) possible next item
                i = len(item.pointers)-1

    def _repr(self):
        for x in self:
            print('%-4s'%x, x.pointers)
        print()


def test():
    n_items = 5
    sl = SkipList()
    for x in range(n_items):
        sl.ll.add(x)
    ll = sl.ll
    sl.first = ll.first

    l = list(sl)
    l[0].add(l[2])
    l[0].add(None)
    l[2].add(None)
    sl.add(6)
    sl._repr()
    sl.add(5)
    sl.def_n = 1
    sl._repr()

test()
