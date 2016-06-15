
def getitem(lst, i, default=None):
    try:
        return lst[i]
    except IndexError:
        return default


class LinkedList:
    def __init__(self):
        self.last = self.first = None

    def add(self, val):
        node = Node(val)
        if self.last is not None:
            self.last.add(node)
            self.last = node
        else:
            self.last = node
        if self.first is None:
            self.first = node

    def __iter__(self):
        item = self.first
        while item:
            yield item
            item = item[0]
        yield item

class Item:
    "Item includes node and the linked list level."
    def __init__(self, node, level):
        self.node,self.level=node,level

    def __len__(self):
        return len(self.node)

    def __repr__(self):
        return '<I: node=%s[%s]>'%(self.node.val,self.level)

    @property
    def pointer(self):
        return self.node.get(self.level)

    def set_pointer(self, node):
        self.node[self.level] = node

class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.pointers=[next] if next is not None else []

    def __getitem__(self, n):
        return self.pointers[n]

    def __setitem__(self, n, val):
        self.pointers[n] = val

    def __repr__(self):
        return '<%s>'%str(self.val)

    def __len__(self):
        return len(self.pointers)

    def __iter__(self):
        return iter(self.pointers)

    def __lt__(self, v):
        return self.val < v

    def __gt__(self, v):
        return self.val > v

    def get(self, n):
        try: return self.pointers[n]
        except IndexError: return None

    def extend(self, seq):
        self.pointers.extend(seq)

    def add(self, v):
        self.pointers.append(v)

    def has_pointers(self):
        return len(self.pointers)

    def has_real_pointers(self):
        return any(1 for p in self.pointers if p is not None)
