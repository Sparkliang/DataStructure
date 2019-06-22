# Data Structure-Ch6 Binary Tree and Tree
# Binary Tree based Class
# Liang
# 2019/5/1

# Construct Binary Tree Node Class
class BinTNode:
    def __init__(self, dat, left = None, right = None):
        self.data = dat
        self.left = left
        self.right = right

# Count node of Binary Tree
def count_BinTNode(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNode(t.left) \
                + count_BinTNode(t.right)

# Supposed that Nodes store numerical value,
# Calculate the sum of all these value
def sum_BinTNode(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNode(t.left) \
                + sum_BinTNode(t.right)

# Recursively defined traversal function
# Root order traversal
def preorder(t, proc): # proc is some operation of Node data
    if t is None:
        proc(t.data)
        preorder(t.left, proc)
        preorder(t.right, proc)

def print_BinTNode(t):
    if t is None:
        print("^", end = "")
        return
    print("(" + str(t.data), end="")
    print_BinTNode(t.left)
    print_BinTNode(t.right)
    print(")", end="")

# Width first traversal
from SQueue import *
from SStack import SStack

def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)

def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while  t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()

def preorder_elements(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()

def postorder(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right

        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None

# Binary Tree Class
class BinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild

    def preorder_elements(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()


