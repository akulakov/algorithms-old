#!/usr/bin/env python3

# https://hg.python.org/cpython/file/52f68c95e025/Objects/dictobject.c#l33

import timeit, string
import sys
from itertools import chain

def int_overflow(val):
  if not -sys.maxsize-1 <= val <= sys.maxsize:
    val = (val + (sys.maxsize + 1)) % (2 * (sys.maxsize + 1)) - sys.maxsize - 1
  return val

txt = open("pg1661.txt").read().replace('\n', ' ').replace('\r', ' ').split(' ')
rm_punct = lambda x: \
    ''.join(a for a in x if a not in string.punctuation)
NUMWORDS=1700
words = txt[500:500+NUMWORDS]
words = sorted(list(set(filter(None, map(rm_punct, words)))))

# words = ['a'*10 +c*10  for c in string.ascii_letters]
# print ("words", words)
lwords = len(words)
print("len(words)", len(words))
SIZE=int(NUMWORDS*1.5)

def h(val, mult=3, seed=0, size=SIZE):
    x = seed
    for c in val:
        x = int_overflow((mult*x + ord(c)))
        # x = (1000003*x ^ ord(c)) % size
        # ord(c)
    # return x % size
    return x

for c in string.ascii_letters:
    print(c, h(c, 13, 103), bin(h(c)))

print()

def test_hash(f, *args):
    hashes = set([f(x, *args)%SIZE for x in words]); lhashes = len(hashes)
    print("%s%s, len(hashes)"%(f.__name__,args), len(hashes), '%.2f' % (lhashes/lwords), '\n')
    return hashes

# test_hash(h)
# test_hash(h, 13)
# test_hash(hash)

hash1,hash2 = {},{}
for w in words:
    h1, h2 = h(w), h(w,1000003,234567)
    # if h1 in hash1: print("w,h1", w, hash1[h1], h1)
    if h2 in hash2: print("w,h2", w, hash2[h2], h2)
    hash1[h1] = w
    hash2[h2] = w

class Dict:
    def __init__(self):
        self.filled = 0
        self.size = 4
        self.table = [None] * 4
        self.collisions = 0
        self.longest_collision=0

    def hash(self, val, mult=13, seed=0):
        x = seed
        for c in val:
            x = int_overflow((mult*x + ord(c)))
        return x

    def __setitem__(self, name, val):
        """ Set key `name` to value `val`.

            Open addressing scheme; works in reverse direction in order to avoid perf. degradation
            with common case of sequential keys going in forward direction; still has degradation
            with sequential keys going back or unordered. (therefore don't use this code in production).
        """
        i = end = self.hash(name) % self.size
        c = 0
        while True:
            if self.table[i] is None:
                break
            self.collisions+=1
            c += 1
            i = (i-1) % self.size
            if i == end:
                break

        self.longest_collision = max(self.longest_collision, c)
        self.table[i] = self.hash(name), name, val
        self.filled += 1
        if self.filled/self.size >= 2/3:
            self.resize_up()

    def resize_up(self):
        self.size *= 2
        old = self.table
        self.table = [None] * self.size
        self.filled = 0
        self.collisions = 0
        for _, name, val in filter(None, old):
            self[name] = val

    def info(self):
        print("self.filled, self.size, self.collisions, self.longest_collision", self.filled,self.size,self.collisions, self.longest_collision)

    def __getitem__(self, name):
        hashed_name = self.hash(name)
        i = self.hash(name) % self.size
        end = i + 1
        while i != end:
        # for i in chain(range(i, self.size-1), range(i)):
            if self.table[i][0] == hashed_name and self.table[i][1] == name:
                return self.table[i][2]
            i = (i-1) % self.size

d = Dict()
d.info()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d.info()
for w in words:
    d[w] = w, len(w)
for i in range(5,100,10):
    w=words[i]
    print(w, d[w])
# print('b', d['b'])
d.info()

# print("hashes", hashes)

# print(timeit.timeit("h(txt)", globals=globals(), number=10))
# print(timeit.timeit("hash(txt)", globals=globals(), number=10))
# print(h(txt))
a = 3
# for x in range(10,20):
    # a = (a * 3 * x) % 2**32
    # print("a,bin(a) %-15s  %35s"% (a,bin(a)))
