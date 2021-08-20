from src.chap2.bubble_sort import bubble_sort


def test_bubble_sort_empty():
    a1 = []
    bubble_sort(a1)
    assert a1 == []


def test_bubble_sort_one_element():
    a2 = [1]
    bubble_sort(a2)
    assert a2 == [1]


def test_bubble_sort_case_one():
    a3 = [2, 4, 3, 6, 5, 1]
    bubble_sort(a3)
    assert a3 == [1, 2, 3, 4, 5, 6]
