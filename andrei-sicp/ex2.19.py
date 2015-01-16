#!/usr/bin/env python3
import operator
p = print

l = [[],[],[]]

def count_change(amount, coin_list, kinds_of_coins=None, d=0):
    """2.19: Count change algorithm."""
    # 2.19 answer: order of coin_list does not affect answer
    def first_denom(n):
        return {m+1:c for m,c in enumerate(coin_list)}[n]
    if kinds_of_coins is None:
        kinds_of_coins = len(coin_list)

    star = '*' if amount==0 else ' '
    if kinds_of_coins:
        l[d].append("%s %d] amount, kinds_of_coins %s %s" % (star, d, amount,kinds_of_coins))
    if amount == 0:
        return 1
    if amount<0 or kinds_of_coins==0:
        return 0
    else:
        amount2 = amount - first_denom(kinds_of_coins)
        # print("amount2", amount2)
        return count_change(amount, coin_list, kinds_of_coins-1, 1) + \
               count_change(amount2, coin_list, kinds_of_coins, 2)

print("CC", count_change(100, [5,1,50,25,10]))
for m in l[1]:
    print(m)
print()
for m in l[2]:
    print(m)
