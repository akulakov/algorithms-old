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
        self.val=val
        self.left=self.right=self.parent=None
        self.height=1

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
        node = node or self.root
        global x
        x+=1
        if x>50:return
        ret = ""
        if node.right is not None:
            ret += self.display(node.right, depth + 1)
        ret += "\n" + (' '*8*depth) + str(node)
        if node.left is not None:
            ret += self.display(node.left, depth + 1)
        return ret + '\n'

    def find(self, val, node=None, path=None, delete=False):
        node = node or self.root
        path = path or []
        path.append(node)
        if val==node.val:
            if delete:
                self.delete_node(node, path[:-1])
            return True
        elif val>node.val:
            if not node.right:
                return None
            return self.find(val, node.right, path, delete)
        elif val<node.val:
            if not node.left:
                return None
            return self.find(val, node.left, path, delete)

    def update_link(self, parent, node, new):
        if parent:
            if parent.right==node: parent.right=new
            if parent.left==node: parent.left=new

    def delete_node(self, node, path):
        is_root = node==self.root
        parent = path[-1] if path else None
        print('deleting', node, 'parent', parent)
        if not (node.right or node.left):
            if is_root:
                self.root = None
            else:
                self.update_link(parent, node, None)

        elif node.right and node.left:
            new=node.right
            path2=[node]    # we may need new's parent
            while new.left:
                path2.append(new)
                new=new.left
            self.delete_node(new, path2)
            if is_root:
                self.root=new
            else:
                self.update_link(parent, node, new)
            new.right, new.left = node.right, node.left

        elif node.right:
            if is_root:
                self.root = node.right
            else:
                self.update_link(parent, node, node.right)
        elif node.left:
            if is_root:
                self.root = node.left
            else:
                self.update_link(parent, node, node.left)


    def add(self, val, node=None, path=None):
        node = node or self.root
        path = path or []
        path.append(node)
        created=0
        if val<node.val:
            if node.left:
                self.add(val, node.left, path)
            else:
                node.left = Node(val, node)
                created=1

        elif val>node.val:
            if node.right:
                self.add(val, node.right, path)
            else:
                node.right = Node(val, node)
                created=1

        if created:
            path.reverse()
            print("added", val)
            print("len(path)", len(path), path)

            for i,n in enumerate(path):
                n.recalc_height()
                next = getitem(path, i+1)
                if n.balance >= 2:
                    if n.right.balance >= 1:
                        print("left rotation")
                        self.rot_left(n, next)
                    elif n.right.balance <= -1:
                        print("double right rotation")
                        self.rot_right(n.right, n)
                        self.rot_left(n, next)

                elif n.balance <= -2:
                    if n.left.balance <= -1:
                        print("right rotation")
                        self.rot_right(n, next)
                    elif n.left.balance <= -1:
                        print("double left rotation")
                        self.rot_left(n.left, n)
                        self.rot_right(n, next)
                # n.height = max(n.height, i+2)

    def rot_right(self, node, parent=None):
        if node==self.root:
            self.root = node.left
        left = node.left
        # print("node", node)
        # print("left", left)
        node.left.right, node.left = node, node.left.right
        node.recalc_height()
        left.recalc_height()

        if parent and parent.right==node:
            parent.right = left
        elif parent and parent.left==node:
            parent.left = left

    def rot_left(self, node, parent=None):
        # print(repr_tree(root))
        if node==self.root:
            self.root = node.right
        right=node.right
        node.right.left, node.right = node, node.right.left
        node.recalc_height()
        right.recalc_height()
        if parent and parent.right==node:
            parent.right = right
        elif parent and parent.left==node:
            parent.left = right


nodes = []
def Xprint_tree(node, indent=0):
    """Print tree recursively, doesn't work well in some corner cases but looks clear enough."""
    nodes.append(node)
    print(' '*indent + str(node))
    if node.left:
        print_tree(node.left, indent+4)
    if node.right:
        print_tree(node.right, indent+4)

x=0

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
tree = Tree(10)
def test2():
    lst= list(n_rand(5))
    for n in lst:
    # for n in (28,31,35,61): #,62,95):
        tree.add(n)
    print("DELETING %s"%lst[0])
    print(tree.display())
    print()
    print("del %s: "%lst[0], tree.find(lst[0], delete=True))
    print(tree.display())
test2()
