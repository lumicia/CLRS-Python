from src.chap6.max_heap import MaxHeap


def test_max_heapify():
    a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heap = MaxHeap(a)
    heap.max_heapify(1)
    assert heap == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]


def test_build_max_heap():
    a = [23, 17, 14, 6, 13, 10, 1, 5, 7, 12]
    heap = MaxHeap(a)
    heap.build_max_heap()
    assert heap == [23, 17, 14, 7, 13, 10, 1, 5, 6, 12]


def test_heap_sort_epmty():
    a1 = []
    heap1 = MaxHeap(a1)
    heap1.heap_sort()
    assert heap1 == []


def test_heap_sort_one_element():
    a2 = [1]
    heap2 = MaxHeap(a2)
    heap2.heap_sort()
    assert heap2 == [1]


def test_heap_sort_case_one():
    a3 = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    heap3 = MaxHeap(a3)
    heap3.heap_sort()
    assert heap3 == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]


def test_heap_sort_case_two():
    a4 = [8, 1, 3, 2, 16, 9, 14, 10, 4, 7]
    heap4 = MaxHeap(a4)
    heap4.heap_sort()
    assert heap4 == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
