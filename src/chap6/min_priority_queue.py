import sys
from typing import Any
from src.chap6.min_heap import MinHeap


class MinPriorityQueue(MinHeap):
    def heap_minimum(self):
        return self[0]

    def heap_extract_min(self) -> Any:
        if self.heap_size < 1:
            sys.exit("heap underflow")

        minimum = self[0]
        self[0] = self[self.heap_size - 1]
        self.heap_size = self.heap_size - 1
        self.min_heapify(0)

        return minimum

    def heap_decrease_key(self, i: int, key: Any) -> None:
        if key > self[i]:
            sys.exit("new key is larger than current key")

        self[i] = key

        while i > 0 and self[self.parent(i)] > self[i]:
            tmp = self[self.parent(i)]
            self[self.parent(i)] = self[i]
            self[i] = tmp
            i = self.parent(i)

    def min_heap_insert(self, key: Any) -> None:
        if self.heap_size >= self.length:
            sys.exit("heap overflow")

        self.heap_size = self.heap_size + 1
        self[self.heap_size - 1] = float("Inf")
        self.heap_decrease_key(self.heap_size - 1, key)
