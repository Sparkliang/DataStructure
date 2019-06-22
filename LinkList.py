# Data Structure-Ch3 Linear List
# Single/Double Linked List, Single/Double Circular Linked List
# Liang
# 2019/4/1

# List Node
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

    def length(self, head): # 利用链表的扫描
        p, n = head, 1
        while p is not None:
            n += 1
            p = p.next
        return n

# Error Class
class LinkedListUnderflow(ValueError):
    pass

# Single Linked List
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    # front end operation
    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e
    # rear end operation
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head  is None: # Empty LList
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None: # till p.next is last node
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    # Other Operation
    def find(self, pred): # pred maybe a function
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    # Reverse
    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next # 摘下原来的首结点
            q.next = p
            p = q
        self._head = p

# Traversal of List
    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

# Sort
    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

    # By adjust Link relationships

    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return

        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p

# Deformed Single Linked List
class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None
    def prepend(self, elem):
        """
        self._head = LNode(elem, self._head)
        if self._head is None: # it is empty list
            self._rear = self._head
        """
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:  # is empty list
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:      # there is only one element in the list
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:  # till p.next is the last one node
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

# Circular Single Linked List
class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem): # Front end insertion
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self): # Front end popup
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

# Double Linked List Node
class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

# Double Linked List
class DLList(LList1):
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last DLList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e


