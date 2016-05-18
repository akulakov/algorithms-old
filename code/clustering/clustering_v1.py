#!/usr/bin/env python3

import sys
import shelve

clusters  = []
dists     = {}
i2cluster = {}
separated = set()


def sorted_tuple(i1, i2):
    """Sorted tuple to avoid duplicate pairs."""
    return tuple(sorted([i1,i2]))

class Pair:
    def __init__(self, i1, i2, dist):
        self.i1, self.i2, self.dist = int(i1), int(i2), int(dist)

    def __iter__(self):
        """Sorted to normalize duplicate pairs."""
        return iter(sorted([self.i1, self.i2]))

    def __hash__(self):
        return hash(tuple(self))

    def __lt__(self, p):
        return self.dist < p.dist

class Cluster:
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
        """Merge `cluster2` into this cluster."""
        # print("joining %s and %s" % (self, c))
        for i1 in self:
            for i2 in cluster2:
                tup = sorted_tuple(i1,i2)
                separated.remove(tup)
                i2cluster[i2] = self
        self.items.extend(cluster2.items)
        clusters.remove(cluster2)


def main():
    """Load data into data structures."""
    data = shelve.open("data")
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

    sep = set()     # in case there are duplicate pairs in source data
    for x,y,dist in data["items"]:
        x,y,dist = int(x), int(y), int(dist)
        tup = sorted_tuple(x,y)
        sep.add((dist, tup))
        separated.add(tup)
        dists[tup] = dist
        Cluster(x); Cluster(y)

        if 0:
            print("sep", sep)
            print("dists", dists)
            print("i2cluster", i2cluster)
            print("clusters", clusters)
            if input('>')=='q': sys.exit()
    return sorted(list(sep), reverse=True)

def cluster(k=10):
    while len(clusters) > k:
        dist, tup = items.pop()
        if tup in separated:
            i1, i2 = tup
            c1, c2 = i2cluster[i1], i2cluster[i2]
            c1.join_cluster(c2)

if __name__ == "__main__":
    items = main()
    argv = sys.argv[1:]
    cluster(int(argv[0]) if argv else 10)
    print("len(clusters)", len(clusters))

    for c in clusters:
        print(c, len(c), "\n\n")
