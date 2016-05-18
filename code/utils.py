from itertools import zip_longest
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

# print(list(grouper('abcdefg', 3)))
def revstr(s):
    return ''.join(reversed(list(s)))

def a(i):
    sp = ' '
    x = sp.join([''.join(g) for g in grouper(revstr(str(i)), 3, sp)])
    return revstr(x)
print(a(2**63))
