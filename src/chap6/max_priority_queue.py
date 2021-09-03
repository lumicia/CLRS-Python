import sys
from typing import Any
from src.chap6.max_heap import MaxHeap


class MaxPriorityQueue(MaxHeap):
    def heap_maximum(self) -> Any:
        return self[0]

    def heap_extract_max(self) -> Any:
        if self.heap_size < 1:
            sys.exit("heap underflow")

        maximum = self[0]
        self[0] = self[self.heap_size - 1]
        self.heap_size = self.heap_size - 1
        self.max_heapify(0)

        return maximum

    def heap_increase_key(self, i: int, key: Any) -> None:
        if key < self[i]:
            sys.exit("new key is smaller than current key")

        self[i] = key

        while i > 0 and self[self.parent(i)] < self[i]:
            tmp = self[self.parent(i)]
            self[self.parent(i)] = self[i]
            self[i] = tmp
            i = self.parent(i)

    def max_heap_insert(self, key: Any) -> None:
        if self.heap_size >= self.length:
            sys.exit("heap overflow")

        self.heap_size = self.heap_size + 1
        self[self.heap_size - 1] = float("-inf")
        self.heap_increase_key(self.heap_size - 1, key)

    def heap_delete(self, i: int) -> None:
        self.heap_increase_key(i, float("inf"))
        self[0], self[self.heap_size - 1] = self[self.heap_size - 1], self[0]
        self.heap_size = self.heap_size - 1
        self.max_heapify(0)
