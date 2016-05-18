#!/usr/bin/env python3

import sys
import shelve
from UnionFind import UnionFind

union = UnionFind()

def sorted_tuple(a, b):
    return tuple(sorted([a,b]))

class Pair:
    """ Pair of items, `i1` and `i2`, with `dist` between them.

        Sortable, hashable and comparable.
        join_clusters() - merge cluster of i2 into the cluster of i1.
    """
    __slots__ = ("i1", "i2", "dist", "tup")

    def __init__(self, i1, i2, dist=None):
        self.i1, self.i2 = int(i1), int(i2)
        self.dist = dist if dist is None else int(dist)
        # sorted to normalize duplicate pairs
        self.tup = tuple(sorted([self.i1, self.i2]))
        # frozenset provides minor speed-up
        # self.tup = frozenset((self.i1, self.i2))

    def __repr__(self):
        return repr(self.tup)

    def __eq__(self, p):
        return self.tup == p.tup

    def __hash__(self):
        return hash(self.tup)

    def __lt__(self, p):
        return self.dist < p.dist


def main():
    """Load data into data structures, return sorted list of item pairs."""
    data = shelve.open("data")
    # load data into the shelve
    if "items" not in data or not data["items"]:
        lst = []
        with open("clustering1.txt") as fp:
            next(fp)
            while True:
                try:
                    l = next(fp)
                except StopIteration:
                    break
                x, y, dist = l.strip().split()
                lst.append((x,y,dist))
        data["items"] = lst

    items = data["items"]
    # test with simple data
    if 1:
        items = [
                     (1,2,10),
                     (1,3,2),
                     (1,4,3),

                     (2,3,10),
                     (2,4,12),

                     (3,4,8),
                     ]

    pairs = set()
    # parse data, create pairs and clusters
    for x,y,dist in items:
        pair = Pair(x, y, dist)
        pairs.add(pair)
        union[pair.i1]
        union[pair.i2]
    return sorted(list(pairs), reverse=True)

def is_separated(pair):
    return union[pair.i1] != union[pair.i2]

def cluster(pairs, k=10):
    """Create `k` clusters from pairs."""
    n_clusters = len(union.parents)
    while True:
        if not pairs: break
        pair = pairs.pop()
        if is_separated(pair):
            union.union(pair.i1, pair.i2)
            n_clusters -= 1
            if n_clusters == k:
                return "min separation value: %s %s" % (pair.dist, str(pair))


if __name__ == "__main__":
    pairs = main()
    argv = sys.argv[1:]
    min_sep = cluster(pairs, int(argv[0]) if argv else 10)
    print(min_sep)
