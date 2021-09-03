from src.chap6.min_priority_queue import MinPriorityQueue


def test_init():
    a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
    q = MinPriorityQueue(a)
    assert q == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]


def test_heap_minimum():
    a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
    assert MinPriorityQueue(a).heap_minimum() == 1


def test_heap_extract_min():
    a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
    q = MinPriorityQueue(a)
    assert q.heap_extract_min() == 1
    assert q == [2, 4, 3, 10, 7, 8, 9, 16, 14, 16]


def test_heap_decrease_key():
    a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
    q = MinPriorityQueue(a)
    q.heap_decrease_key(8, 1)
    assert q == [1, 1, 3, 2, 7, 8, 9, 10, 4, 16]


def test_heap_insert():
    a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
    q = MinPriorityQueue(a)
    q.heap_extract_min()
    q.min_heap_insert(0)
    assert q == [0, 2, 3, 10, 4, 8, 9, 16, 14, 7]
