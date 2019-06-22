# Data Structure-Ch3 Linear List
# Sequenced List Sort && Single Linked List Sort
# Liang
# 2019/4/4

# By Moving Elements
def list_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x
    return lst

# By Moving Elements
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