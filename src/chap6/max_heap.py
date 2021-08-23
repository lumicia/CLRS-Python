class MaxHeap(list):
    def __init__(self, data: list[int]):
        super().__init__(data)
        self.length = len(self)
        self.heap_size = self.length
        self.build_max_heap()

    @staticmethod
    def parent(i: int) -> int:
        return (i - 1) // 2

    @staticmethod
    def left(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def right(i: int) -> int:
        return 2 * i + 2

    def max_heapify(self, i: int) -> None:
        l = self.left(i)
        r = self.right(i)

        if l <= self.heap_size - 1 and self[l] > self[i]:
            largest = l
        else:
            largest = i

        if r <= self.heap_size - 1 and self[r] > self[largest]:
            largest = r

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(largest)

    def build_max_heap(self) -> None:
        self.heap_size = self.length
        for i in range(self.length // 2 - 1, -1, -1):
            self.max_heapify(i)

    def heap_sort(self) -> None:
        self.build_max_heap()
        for i in range(self.length - 1, 0, -1):
            self[0], self[i] = self[i], self[0]
            self.heap_size -= 1
            self.max_heapify(0)
