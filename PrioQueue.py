# Data Structure-Ch6 Binary Tree and Tree
# Priority Queue
# Liang
# 2019/4/23

class PrioQueueError(ValueError):
    pass

class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()


class PrioQueue:
    """
    Implementing priority queues using heaps
    """

    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None) # add a dummpy element
        self.sifup(e, len(self._elems) - 1)

    def sifup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = 3

    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)

    def heap_sort(self, elems):
        def siftdown(elems, e, begin, end):
            i, j = begin, begin*2+1
            while j < end:
                if j+1 < end and elems[j+1] < elems[j]:
                    j += 1
                if e < elems[j]:
                    break
                elems[i] = elems[j]
                i, j = j, 2*j+1
            elems[i] = e
        end = len(elems)
        for i in range(end//2, -1, -1):
            siftdown(elems, elems[i], i, end)
        for i in range((end-1), 0, -1):
            e = elems[i]
            elems[i] = elems[0]
            siftdown(elems, e, 0, i)

