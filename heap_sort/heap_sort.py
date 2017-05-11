from math import floor


class Heap:

    def __init__(self, it):
        self._heap_size = len(it)
        self._heap = self._build_heap(it)

    def get_heap(self):
        return self._heap

    @staticmethod
    def _parent(i):
        return floor(i / 2)

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _right(i):
        return 2 * i + 2

    @staticmethod
    def _swap(it, i, j):
        tmp = it[i]
        it[i] = it[j]
        it[j] = tmp

    def _build_heap(self, it):
        for i in range(floor(self._heap_size / 2), -1, -1):
            self._heapify(it, i)

        return it

    def _heapify(self, it, i):
        l = self._left(i)
        r = self._right(i)

        if l < self._heap_size and it[l] > it[i]:
            largest = l
        else:
            largest = i

        if r < self._heap_size and it[r] > it[largest]:
            largest = r

        if largest != i:
            self._swap(it, i, largest)
            self._heapify(it, largest)

    def sort(self):
        for i in range(self._heap_size - 1, 0, -1):
            self._swap(self._heap, 0, i)
            self._heap_size -= 1
            self._heapify(self._heap, 0)

        return self._heap
