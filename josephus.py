# Data Structure-Ch3 Linear List
# Josephus Problem
# Liang
# 2019/4/5

# Based on Array
from DataStructure.LinkList import LCList


def josephus_A(n, k, m):
    people = list(range(1, n+1))

    i = k-1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i+1)%n
        if num < n-1:
            print(", ", end="")
        else:
            print("")
    return

# Based on sequence list
def josephus_L(n, k, m):
    people = list(range(1, n+1))

    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i+m-1) % num
        print(people.pop(i), end=(", " if num > 1 else "\n"))
    return

# Based on Circular Single Linked List
class Josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next
    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(),
                  end=("\n" if self.is_empty() else ", "))
