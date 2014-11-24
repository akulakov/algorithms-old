#!/usr/bin/env python3

from collections import Counter

cards = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']

def all_same(seq):
    """All items in `seq` are the same; empty seq returns True."""
    return len(set(seq)) == 1


class Card:
    def __init__(self, card):
        self.card, self.suit = card
        d         = dict(T=10, J=11,Q=12,K=13,A=14)
        self.val  = d.get(card) or int(card)

    def __repr__(self):
        return self.card + self.suit

    def __lt__(self, card):
        return self.val < card.val


class Hand:
    def __init__(self, hand):
        self.cards = []
        for c in hand.split():
            self.cards.append(Card(c))
        self.cards.sort()
        self.nominals  = [c.card for c in self.cards]
        self.values    = [c.val for c in self.cards]
        self.suits     = [c.suit for c in self.cards]
        self.val_count = Counter(self.values)

    def __repr__(self):
        return ' '.join(str(c) for c in self.cards)

    def rflush(self):
        """Royal flush."""
        return set(self.nominals) == set("JQKAT") and all_same(self.suits)

    def sflush(self):
        """Straight flush."""
        return all_same(self.suits) and self.in_sequence()

    def n_of_a_kind(self, n):
        return [v for v, count in self.val_count.items() if count==n]

    def of_a_kind_4(self): return self.n_of_a_kind(4)
    def of_a_kind_3(self): return self.n_of_a_kind(3)
    def of_a_kind_2(self): return self.n_of_a_kind(2)

    def full_house(self):
        n3, n2 = self.of_a_kind_3(), self.of_a_kind_2()
        # note: return value types need to be comparable
        if n3 and n2:
            return n3, n2
        else:
            return []

    def flush(self):
        return all_same(self.suits)

    def straight(self):
        return self.in_sequence()

    def in_sequence(self):
        v0 = self.values[0]
        return self.values == list(range(v0, v0+5))

    def two_pairs(self):
        lst = self.of_a_kind_2()
        # note: return value types need to be comparable
        if len(lst) == 2:
            return sorted(lst, reverse=True)
        else:
            return []

    def compare_cards(self):
        """ Compare cards by value; hand wins if a higher value card occurs sooner in sorted list.

            Note: given small number of cards in hand it's easier to compare sorted lists, if # of
            cards was very large, it would be best to create reversed list originally and pop cards
            one by one.
        """
        return list(reversed(self.values))

    def __lt__(self, other):
        tests = """\
                    rflush
                    of_a_kind_4
                    full_house
                    flush
                    straight
                    of_a_kind_3
                    two_pairs
                    of_a_kind_2
                    compare_cards\
                """.split()

        for m in tests:
            t1 = getattr(self, m)()
            t2 = getattr(other, m)()
            if t1 != t2:
                print(m)
                return t2>t1


def test1():
    h = """\
            5H 5C 6S 7S KD
            2C 3S 8S 8D TD

            5D 8C 9S JS AC
            2C 5C 7D 8S QH

            2D 9C AS AH AC
            3D 6D 7D TD QD

            4D 6S 9H QH QC
            3D 6D 7H QD QS

            2H 2D 4C 4D 4S
            3C 3D 3S 9S 9D
    """
    h = h.split("\n\n")
    for hand in h:
        h1, h2 = [h.strip() for h in hand.strip().splitlines()]
        # print("h1,h2", h1, ';', h2)
        h1, h2 = Hand(h1), Hand(h2)
        print("===", "p1 wins" if h1>h2 else "p2 wins")

test1()
