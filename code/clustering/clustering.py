#!/usr/bin/env python3

import sys
import shelve

clusters  = []
separated = set()
i2cluster = {}      # item to cluster mapping


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
        # self.tup = frozenset((self.i1, self.i2))

    def __repr__(self):
        return repr(self.tup)

    def __eq__(self, p):
        return self.tup == p.tup

    def __hash__(self):
        return hash(self.tup)

    def __lt__(self, p):
        return self.dist < p.dist

    def join_clusters(self):
        c1, c2 = i2cluster[self.i1], i2cluster[self.i2]
        c1.join_cluster(c2)


class Cluster:
    __slots__ = ("items",)

    def __init__(self, item):
        """ Init cluster with a single starting `item`.
            If this item's cluster already exists, do nothing.
        """
        if item not in i2cluster:
            self.items = [item]
            i2cluster[item] = self
            clusters.append(self)

    def __repr__(self):
        return "[%s]" % (' '.join([str(i) for i in self.items]))

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def join_cluster(self, cluster2):
        """ Merge `cluster2` into this cluster.

            - remove all combinations of clusters' pairs from `separated` set
            - update `cluster2`'s items to be in this cluster
            - remove `cluster2`
        """
        # print("joining %s and %s" % (self, c))
        for i1 in self:
            for i2 in cluster2:
                separated.remove(Pair(i1,i2))
                i2cluster[i2] = self
        self.items.extend(cluster2.items)
        clusters.remove(cluster2)


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
    if 0:
        items = [
                     (1,2,10),
                     (1,3,2),
                     (1,4,3),

                     (2,3,10),
                     (2,4,12),

                     (3,4,8),
                     ]

    # parse data, create pairs and clusters
    for x,y,dist in items:
        pair = Pair(x, y, dist)
        separated.add(pair)
        Cluster(pair.i1)
        Cluster(pair.i2)
        if 0:
            if input('>')=='q': sys.exit()
    return sorted(list(separated), reverse=True)

def cluster(pairs, k=10):
    """Create `k` clusters from pairs."""
    while True:
        if not pairs: break
        pair = pairs.pop()
        if pair in separated:
            if len(clusters) == k:
                return "min separation value: %s %s" % (pair.dist, str(pair))
            pair.join_clusters()


if __name__ == "__main__":
    pairs = main()
    argv = sys.argv[1:]
    min_sep = cluster(pairs, int(argv[0]) if argv else 10)
    for c in clusters:
        print(c, len(c), "\n\n")
    print("len(clusters)", len(clusters))
    print(min_sep)
