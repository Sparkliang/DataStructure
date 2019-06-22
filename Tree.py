# Data Structure-Ch6 Binary Tree and Tree
# Tree based list
# Liang
# 2019/5/3

class SubtreeIndexError(ValueError):
    pass

def Tree(data, *a):
    #return [data].extend(a)
    list1 = [data]
    list2 = a
    list1.extend(list2)
    return list1


def is_empty_Tree(tree):
    return tree is None

def root(tree):
    return tree[0]

def subtree(tree, i):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    return tree[i+1]

def set_root(tree, data):
    tree[0] = data

def set_subtree(tree, i, subtree):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i+1] = subtree
