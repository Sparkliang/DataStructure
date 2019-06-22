# Data Structure-Ch8 Dictionary and set
# Dictionary Binary Tree
# Liang
# 2019/6/19

from BinTreeClass import BinTNode
from SStack import SStack

class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, other):
        return self.key < other.key
    def __le__(self, other):
        return self.key < other.key or self.key == other.key
    def __str__(self):
        return "Assoc({0},{1})".format(self.key, self.value)

class DictList:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def num(self):
        pass

def bt_search(btree, key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key < entry.key:
            bt = bt.left
        elif key > entry.key:
            bt = bt.right
        else:
            return entry.value
    return None

class DictBinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.left is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return

    def values(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.value
            t = t.right

    def entries(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            s.push(t)
            t = t.left
        t = s.pop()
        yield t.data.key, t.data.value
        t = t.right

    def delete(self, key):
        p, q = None, self._root
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None:
                return

            if q.left is None:
                if p is None:
                    self._root = q.right
                elif q is p.left:
                    p.left = q.right
                else:
                    p.right = q.right
                return

            r = q.left
            while r.right is not None:
                r = r.right
            r.right = q.right
            if p is None:
                self._root = q.left
            elif p.left is q:
                p.left = q.left
            else:
                p.right = q.left

    def print(self):
        for k, v in self.entries():
            print(k, v)

    # END class

def build_dictBinTree(entries):
    dic = DictBinTree()
    for k, v in entries:
        dic.insert(k, v)
    return dic

class DictOptBinTree(DictBinTree):
    def __init__(self, seq):
        DictBinTree.__init__(self)
        data = sorted(seq)
        self._root = DictOptBinTree.buildOBT(data, 0, len(data)-1)

    @staticmethod
    def buildOBT(data, start, end):
        if start > end:
            return None
        mid = (end + start) // 2
        left = DictOptBinTree.buildOBT(data, start, mid-1)
        right = DictOptBinTree.buildOBT(data, mid+1, end)
        return BinTNode(Assoc(*data[mid]), left, right)
    