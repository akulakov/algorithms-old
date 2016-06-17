#!/usr/bin/env python3

from random import randint

def getitem(seq, i):
    try: return seq[i]
    except IndexError: return None

def n_rand(n):
    "Set of `n` random nums from 0 to 100."
    s = set()
    while len(s) < n:
        s.add(randint(0,100))
    return s

class Node:
    "Node has height attribute and calculates balance based on heights of children."
    def __init__(self, val, parent=None):
        self.val = val
        self.left = self.right = self.parent = None
        self.height = 1

    @property
    def balance(self):
        return getattr(self.right, "height", 0) - getattr(self.left, "height", 0)

    def __repr__(self):
        return "%s [%s] [h:%s]" % (str(self.val), self.balance, self.height)

    def recalc_height(self):
        self.height = max(getattr(self.left, "height", 0), getattr(self.right, "height", 0)) + 1


class Tree:
    def __init__(self, val):
        self.root = Node(val)

    def display(self, node=None, depth=0):
        "Return string to display; right children on top, left children on the bottom."
        if self.root is None:
            return None
        node = node or self.root
        # global x
        # x+=1
        # if x>50:return
        ret = ""
        if node.right is not None:
            ret += self.display(node.right, depth + 1)
        ret += "\n" + (' '*8*depth) + str(node)
        if node.left is not None:
            ret += self.display(node.left, depth + 1)
        return ret + '\n'

    def remove(self, val):
        return self.find(val, delete=True)

    def find(self, val, node=None, path=None, delete=False):
        "Find `val` under `node`, optionally delete if `delete` is True."
        if not self.root:
            return None
        node = node or self.root
        path = path or []
        if val==node.val:
            if delete:
                self.delete_node(node, path)
            return True
        else:
            next = node.right if val>node.val else node.left
            if not next:
                return None
            return self.find(val, next, path+[node], delete)

    def replace_node(self, parent, a, b):
        """ Replace old `node` with `new` node, updating parent's link.
            if node is root, update root link instead.
        """
        if a==self.root:
            self.root = b
        else:
            if parent.right==a: parent.right = b
            if parent.left==a: parent.left = b

    def delete_node(self, node, path):
        """Delete `node`."""
        parent = getitem(path, -1)
        if not any([node.right, node.left]):
            self.replace_node(parent, node, None)
            self.rebalance(path)

        elif node.right and node.left:
            new = node.right
            # path2 = [node]
            path.append(node)
            while new.left:
                path.append(new)
                new = new.left
            self.delete_node(new, path)
            self.replace_node(parent, node, new)
            new.right, new.left = node.right, node.left
        else:
            self.replace_node(parent, node, node.right or node.left)
            self.rebalance(path)

    def add(self, val, node=None, path=None):
        "Add `val` to the tree."
        node = node or self.root
        path = path or []
        path.append(node)
        created = 0
        if val<node.val:
            if node.left:
                self.add(val, node.left, path)
            else:
                node.left = Node(val, node)
                created = 1

        elif val>node.val:
            if node.right:
                self.add(val, node.right, path)
            else:
                node.right = Node(val, node)
                created = 1

        if created:
            self.rebalance(path)

    def rebalance(self, path):
        # print("path", path)
        path.reverse()
        for i,n in enumerate(path):
            n.recalc_height()
            next = getitem(path, i+1)
            if n.balance >= 2:
                if n.right.balance >= 0:
                    self.rot_left(n, next)
                elif n.right.balance <= -1:
                    self.rot_right(n.right, n)
                    self.rot_left(n, next)

            elif n.balance <= -2:
                if n.left.balance <= 0:
                    self.rot_right(n, next)
                elif n.left.balance <= -1:
                    self.rot_left(n.left, n)
                    self.rot_right(n, next)

    def rot_right(self, node, parent=None):
        if node==self.root:
            self.root = node.left
        left = node.left
        node.left.right, node.left = node, node.left.right
        node.recalc_height()
        left.recalc_height()

        if parent and parent.right==node:
            parent.right = left
        elif parent and parent.left==node:
            parent.left = left

    def rot_left(self, node, parent=None):
        if node==self.root:
            self.root = node.right
        right = node.right
        node.right.left, node.right = node, node.right.left
        node.recalc_height()
        right.recalc_height()
        if parent and parent.right==node:
            parent.right = right
        elif parent and parent.left==node:
            parent.left = right


def test():
    # root = Node(randint(0,100))
    # add(root, 12)
    add(root, 12)
    # print(print_tree(root))
    print(repr_tree(root))
    print('-'*40)
    add(root, 11)

    print(repr_tree(root))
    print('-'*40)

    rot_right(root.right, root)
    print(repr_tree(root))
    print('-'*40)
    rot_left(root)
    print(repr_tree(root))
    # add(root, 4)
    # add(root, 3)
    # print(print_tree(root))

    # for _ in range(10):
        # add(root, randint(0,100))
    # print(print_tree(root))

    # print("nodes", nodes)

# test()
# lst = list(n_rand(5))
lst = 42,17,50,45,95
tree = Tree(lst[0])
def test2():
    # for n in lst[1:]:
    for n in (17,50,45,95): #,62,95):
        tree.add(n)
    to_del=17
    print("DELETING %s"%to_del)
    print(tree.display())
    # for x in lst:
        # print('removing', x)
        # tree.remove(x)
    print("tree.root", tree.root)
    print('-'*79)
    tree.remove(to_del)
    print()
    # print("del %s: "%lst[0], tree.find(lst[0], delete=True))
    print(tree.display())
test2()
