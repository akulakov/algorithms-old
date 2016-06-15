from itertools import zip_longest
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

def revstr(s):
    return ''.join(reversed(list(s)))

def is_seq(x):
    "Non-string sequence?"
    return hasattr(x, "__iter__") and not isinstance(x, str)
