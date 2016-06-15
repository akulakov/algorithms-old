#!/usr/bin/env python3

import heapq
import sys
from collections import Counter
from pprint import pprint

class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return "Node"

    def __lt__(self, x):
        return self.val < len(x)

def make_tree(freq):
    """ Create binary tree where each leaf is an item to be encoded.
        Leaf nodes are in the tree only as values, not as keys, so we can test for leaf nodes by checking in the tree.
    """
    tree = dict()
    assert len(freq)>=2
    while freq:
        i1, i2 = heapq.heappop(freq), heapq.heappop(freq)
        # align consistently to make it easier to display
        # if isinstance(i1[1], Node):
        if i1[1] in tree:
            i1,i2 = i2,i1
        sum = i1[0]+i2[0]
        node = Node(sum)
        tree[node] = i1[1], i2[1]
        heapq.heappush(freq, (sum, node))
        if len(freq) == 1:
            break
    return node, tree

def test_make_tree():
    d = [(1,'a'),(2,'b')]
    heapq.heapify(d)
    n,t = make_tree(d)
    print(n,t)

def make_code(tree, codes, node, code):
    """ Walk the tree, adding to `code` for each recursion into left or right branch.
        Leaf nodes are in the tree only as values, not as keys, so we can test for leaf nodes by checking in the tree.

        codes: dictionary {char: code}
        node: intermediate Node or leaf character node
        code: code being built recursively, completed at each leaf node
    """
    if node in tree:
        left, right = tree[node]
        make_code(tree, codes, left, code + '0')
        make_code(tree, codes, right, code + '1')
    else:
        codes[node] = code

def print_tree(node, tree, codes, indent=0):
    """Print tree recursively, doesn't work well in some corner cases but looks clear enough."""
    tab = 15
    pad = [' '] * indent
    if indent:
        pad[indent-tab] = '|'
        pad[-tab+1:-1] = ['-']*(tab-4)
    print("%s %s  %s" % (''.join(pad), str(node), codes.get(node) or ''))

    if node in tree:
        left, right = tree[node]
        print_tree(left, tree, codes, indent+tab)
        print_tree(right, tree, codes, indent+tab)

def decode(inp, codes):
    """Decode string of codes into original chars."""
    cur = ''
    out = []
    for c in inp:
        cur += c
        if cur in codes:
            out.append(codes[cur])
            cur = ''
    print("decoded:", ''.join(out))

def test_huff_code():
    argv = sys.argv[1:]
    if not argv:
        print("Need a string of chars as an argument")

    freq = [(v,k) for k,v in Counter(argv[0]).items()]
    if len(freq)==1:
        print ("%s: 0" % freq[0][1])
        return
    heapq.heapify(freq)
    root, tree = make_tree(freq)
    codes = {}
    make_code(tree, codes, root, '')
    print_tree(root, tree, codes)
    out = []
    for c in argv[0]:
        out.append(codes[c])
    print("codes", codes)
    print("out", ''.join(out))
    codes = {v:k for k,v in codes.items()}
    decode(out, codes)


test_huff_code()
