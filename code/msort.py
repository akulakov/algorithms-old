ncalls = [0]

def merge_sort(lst):
    """Sorts the input list using the merge sort algorithm.

    >>> lst = [4, 5, 1, 6, 3]
    >>> merge_sort(lst)
    [1, 3, 4, 5, 6]
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    """Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.

    >>> left = [1, 5, 6]
    >>> right = [2, 3, 4]
    >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """
    ncalls[0]+=1
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

from random import randrange, shuffle

def get_n_calls(size):
    ncalls[0] = 0
    lst = list(range(size))
    merge_sort(lst)
    print(size, ncalls[0], ncalls[0]/size if size else 0)

for s in range(0,100,10):
    get_n_calls(s)
