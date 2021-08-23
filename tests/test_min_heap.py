from src.chap6.min_heap import MinHeap


def test_min_heapify():
    a = [1, 2, 3, 14, 7, 8, 9, 10, 4, 16]
    heap = MinHeap(a)
    heap.min_heapify(3)
    assert heap == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]


def test_build_min_heap():
    a = [10, 1, 2, 8, 7, 3, 4, 9, 14, 16]
    heap = MinHeap(a)
    heap.build_min_heap()
    heap == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
