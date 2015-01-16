#!/usr/bin/python3
import sys
import queue
from collections import Counter

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.freq, self.char = val
        self.left, self.right = left, right
        self.is_internal = left!=None or right!=None

    def __lt__(self, other):
        """Needed to make nodes sortable."""
        return self.val < other.val

    def traverse(self, node=None, code=''):
        node = node or self
        indent = ' ' * len(code) * 2
        if not code:
            print ("ROOT %s" % node.freq)
        elif not (node.left or node.right):
            print ("%s Leaf %s => %s" % (indent, node.val, code))
        else:
            print ("%s Internal %s => %s" % (indent, node.freq, code))

        if node.left and node.left.is_internal:
            nodes = [node.right, node.left]
        else:
            nodes = [node.left, node.right]

        # note: breaks the convention where left=0 and right=1
        if nodes[0]:
            self.traverse(nodes[0], code + '0')
        if nodes[1]:
            self.traverse(nodes[1], code + '1')

def build_tree(data):
    nodes = [Node((f,c)) for c,f in Counter(data).items()]
    pq = queue.PriorityQueue()
    for n in nodes:
        pq.put(n)
    while pq.qsize() > 1:
        n1, n2 = pq.get(), pq.get()
        node = Node((n1.freq+n2.freq, ''), n1, n2)
        pq.put(node)
    root = pq.get()
    root.traverse()

inp = sys.argv[1]
build_tree(inp)
