from src.chap2.merge_sort import merge_sort


def test_merge_sort_empty():
    a1 = []
    merge_sort(a1, 0, 0)
    assert a1 == []


def test_merge_sort_one_element():
    a2 = [1]
    merge_sort(a2, 0, 0)
    assert a2 == [1]


def test_merge_sort_case_one():
    a3 = [5, 2, 4, 6, 1, 3]
    merge_sort(a3, 0, 5)
    assert a3 == [1, 2, 3, 4, 5, 6]


def test_merge_sort_reversed():
    a4 = [6, 5, 4, 3, 2, 1]
    merge_sort(a4, 0, 5)
    assert a4 == [1, 2, 3, 4, 5, 6]

