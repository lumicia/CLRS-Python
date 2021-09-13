from src.chap10.queue import Queue


def test_empty_queue():
    q1 = Queue(0)
    assert q1.is_empty() == True


def test_one_element_queue():
    q2 = Queue(1)
    assert q2.is_empty() == True
    q2.enqueue(3)
    assert q2.is_full() == True
    assert q2.dequeue() == 3
    assert q2.is_empty() == True


def test_queue_case_one():
    q3 = Queue(3)
    assert q3.is_empty() == True
    q3.enqueue(2)
    q3.enqueue(7)
    assert q3.is_full() == False
    q3.enqueue(5)
    assert q3.is_full() == True
    assert q3.dequeue() == 2
    assert q3.dequeue() == 7
    assert q3.is_empty() == False
    assert q3.dequeue() == 5
    assert q3.is_empty() == True
