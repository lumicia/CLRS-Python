from typing import Any


class MinHeap(list):
    def __init__(self, data: list[int]):
        super().__init__(data)
        self.length = len(self)
        self.heap_size = self.length
        self.build_min_heap()

    @staticmethod
    def parent(i: int) -> int:
        return (i - 1) // 2

    @staticmethod
    def left(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def right(i: int) -> int:
        return 2 * i + 2

    def min_heapify(self, i: int) -> None:
        l = self.left(i)
        r = self.right(i)

        if l <= self.heap_size - 1 and self[l] < self[i]:
            smallest = l
        else:
            smallest = i

        if r <= self.heap_size - 1 and self[r] < self[smallest]:
            smallest = r

        if smallest != i:
            self[i], self[smallest] = self[smallest], self[i]
            self.min_heapify(smallest)

    def build_min_heap(self) -> None:
        self.heap_size = self.length
        for i in range(self.length // 2 - 1, -1, -1):
            self.min_heapify(i)
