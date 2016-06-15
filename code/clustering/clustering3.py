#!/usr/bin/env python3

from random import randint
from itertools import combinations, product
from heapq import heapify, heappop
from pprint import pprint

"""
is-sep: roots[a] != roots[b] != None
union:
    for x in clusters[a]:
        clusters[b].add(x)
        roots[x] = b
    clusters[b].add(a)
    roots[a] = b
    del clusters[a]

INIT num-clusters
INIT all-pairs with distances
while num-clusters <= K:
    pop a pair
    if pair.is-separate:
        union(pair)
        num-clusters -= num-clusters

make-pair:
    dist, a, b # where a<b
"""

def n_rand(n):
    s = set()
    while len(s) < n:
        s.add(randint(0,100))
    return s

def dist(a,b):
    return abs(a-b)

def make_pair(a,b):
    return (dist(a,b),) + ((a,b) if a<b else (b,a))

def make_clusters(items, k):
    def add_to_cluster(root, item):
        clusters[root].add(item)
        roots[item] = root

    def is_sep(a,b):
        return roots[a] != roots[b]

    def merge(a,b):
        "Merge a into b."
        a,b = roots[a], roots[b]
        for x in list(clusters[a]) + [a]:
            add_to_cluster(x, b)
        del clusters[a]

    pairs = [make_pair(a,b) for a,b in combinations(items, 2)]
    heapify(pairs)
    num_clusters = len(items)
    roots = {x:x for x in items}
    clusters = {x: set() for x in items}

    while num_clusters > k and pairs:
        _,a,b = heappop(pairs)
        if is_sep(a,b):
            merge(a,b)
            num_clusters -= 1

    pprint(clusters, compact=1)
    print("num_clusters", num_clusters)

# items = n_rand(10)
make_clusters(n_rand(50), 6)

# combs = combinations(n_rand(100),2)

# dists = {pair: dist(*pair) for pair in combs}

# print("dists", dists)
