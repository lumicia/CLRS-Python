from src.chap2.insertion_sort import insertion_sort


def test_insertion_sort_empty():
    a1 = []
    insertion_sort(a1)
    assert a1 == []


def test_insertion_sort_one_element():
    a2 = [1]
    insertion_sort(a2)
    assert a2 == [1]


def test_insertion_sort_case_one():
    a3 = [5, 2, 4, 6, 1, 3]
    insertion_sort(a3)
    assert a3 == [1, 2, 3, 4, 5, 6]


def test_insertion_sort_reversed():
    a4 = [6, 5, 4, 3, 2, 1]
    insertion_sort(a4)
    assert a4 == [1, 2, 3, 4, 5, 6]
