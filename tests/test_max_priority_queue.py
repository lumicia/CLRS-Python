from src.chap6.max_priority_queue import MaxPriorityQueue


def test_init():
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    q = MaxPriorityQueue(a)
    assert q == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]


def test_heap_maximum():
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    assert MaxPriorityQueue(a).heap_maximum() == 16


def test_heap_extract_max():
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    h = MaxPriorityQueue(a)
    assert h.heap_extract_max() == 16
    assert h == [14, 8, 10, 4, 7, 9, 3, 2, 1, 1]


def test_heap_increase_key():
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    h = MaxPriorityQueue(a)
    h.heap_increase_key(8, 15)
    assert h, [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]


def test_heap_insert():
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    queue = MaxPriorityQueue(a)
    queue.heap_extract_max()
    queue.max_heap_insert(100)
    assert queue == [100, 14, 10, 4, 8, 9, 3, 2, 1, 7]


def test_heap_delete():
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    h = MaxPriorityQueue(a)
    h.heap_delete(4)
    assert h[0 : h.heap_size] == [16, 14, 10, 8, 1, 9, 3, 2, 4]
    h.heap_delete(2)
    assert h[0 : h.heap_size] == [16, 14, 9, 8, 1, 4, 3, 2]
    h.heap_delete(0)
    assert h[0 : h.heap_size] == [14, 8, 9, 2, 1, 4, 3]
    h.heap_delete(5)
    assert h[0 : h.heap_size] == [14, 8, 9, 2, 1, 3]
    h.heap_delete(3)
    assert h[0 : h.heap_size] == [14, 8, 9, 3, 1]
    h.heap_delete(1)
    assert h[0 : h.heap_size] == [14, 3, 9, 1]
    h.heap_delete(3)
    assert h[0 : h.heap_size] == [14, 3, 9]
    h.heap_delete(2)
    assert h[0 : h.heap_size] == [14, 3]
    h.heap_delete(1)
    assert h[0 : h.heap_size] == [14]
    h.heap_delete(0)
    assert h[0 : h.heap_size] == []
