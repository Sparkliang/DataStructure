# Data Structure-Ch8 Dictionary and set
# Association
# Liang
# 2019/6/16

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


