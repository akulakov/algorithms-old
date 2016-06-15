#!/usr/bin/python
import sys
import heapq
import json
from collections import Counter

# AK implementation

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
            print "ROOT %s" % node.freq
        elif not (node.left or node.right):
            print "%s Leaf %s => %s" % (indent, node.val, code)
        else:
            print "%s Internal %s => %s" % (indent, node.freq, code)

        if node.left and node.left.is_internal:
            nodes = [node.right, node.left]
        else:
            nodes = [node.left, node.right]

        if nodes[0]:
            self.traverse(nodes[0], code + '0')
        if nodes[1]:
            self.traverse(nodes[1], code + '1')

def build_tree3(data):
    nodes = [Node((f,c)) for c,f in Counter(data).items()]
    heapq.heapify(nodes)
    while len(nodes) > 1:
        n1 = heapq.heappop(nodes)
        n2 = heapq.heappop(nodes)
        node = Node((n1.freq+n2.freq, ''), n1, n2)
        heapq.heappush(nodes, node)
    root = heapq.heappop(nodes)
    root.traverse()

# END AK implementation

def traverse(ptree, node, prefix):
    # print("node", node)
    print("ptree[node]", ptree[node])
    left, right = ptree[node]
    indent = ' ' * len(prefix) * 2
    if not (left or right):
        print "%s LEAF '%s' => %s" % (indent, node, prefix)
    else:
        print "%s INTERNAL '%s'" % (indent, node)
    if left:
        traverse(ptree, left, prefix + '0')
    if right:
        traverse(ptree, right, prefix + '1')

def build_tree2(data):
    # array of tuples, each element is a node in the tree
    total = len(data)
    nodes = []
    # prefix tree with keys as lists of characters
    ptree = {} #tree()
    freq = Counter(data)
    for ch in freq:
        #nodes.append((float(freq[ch])/total, ch))
        nodes.append((freq[ch], ch))
    heapq.heapify(nodes)
    print nodes
    while len(nodes) > 1:
        n1 = heapq.heappop(nodes)
        n2 = heapq.heappop(nodes)
        # if the node has not been inserted,
        # it is a leaf node and need to be inserted
        if n1[1] not in ptree:
            ptree[n1[1]] = (None, None)
        if n2[1] not in ptree:
            ptree[n2[1]] = (None, None)
        # create a merged node with frequence = sum of children frequencies
        merged = (n1[1], n2[1])
        merged_key = merged[0] + merged[1]
        # print("merged_key", merged_key)
        ptree[merged_key] = merged
        node = (n1[0] + n2[0], merged_key)
        print("node", node)
        heapq.heappush(nodes, (n1[0] + n2[0], merged_key))
    root = heapq.heappop(nodes)
    assert(root[1] in ptree)
    traverse(ptree, root[1], ' ')
    # print(json.dumps(ptree, indent=4))

def build_tree(data):
    # array of tuples, each element is a node in the tree
    total = len(data)
    nodes = []
    # prefix tree with keys as lists of characters
    ptree = {} #tree()
    freq = Counter(data)
    for ch in freq:
        #nodes.append((float(freq[ch])/total, ch))
        nodes.append((freq[ch], ch))
    heapq.heapify(nodes)
    print nodes
    while len(nodes) > 1:
        n1 = heapq.heappop(nodes)
        n2 = heapq.heappop(nodes)
        # if the node has not been inserted,
        # it is a leaf node and need to be inserted
        if n1[1] not in ptree:
            ptree[n1[1]] = (None, None)
        if n2[1] not in ptree:
            ptree[n2[1]] = (None, None)
        # create a merged node with frequence = sum of children frequencies
        merged = (n1[1], n2[1])
        merged_key = merged[0] + merged[1]
        # print("merged_key", merged_key)
        ptree[merged_key] = merged
        node = (n1[0] + n2[0], merged_key)
        print("node", node)
        heapq.heappush(nodes, (n1[0] + n2[0], merged_key))
    root = heapq.heappop(nodes)
    assert(root[1] in ptree)

    print("ptree", ptree)
    # traverse(ptree, root[1], ' ')
    # print(json.dumps(ptree, indent=4))

# huffman encoding
inp = sys.argv[1]
# print "Input:", inp
build_tree3(inp)
