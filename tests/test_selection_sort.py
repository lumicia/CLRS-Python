from src.chap2.selection_sort import selection_sort


def test_selection_sort_empty():
    a1 = []
    selection_sort(a1)
    assert a1 == []


def test_selection_sort_one_element():
    a2 = [1]
    selection_sort(a2)
    assert a2 == [1]


def test_selection_sort_case_one():
    a3 = [5, 2, 4, 6, 1, 3]
    selection_sort(a3)
    assert a3 == [1, 2, 3, 4, 5, 6]


def test_selection_sort_reversed():
    a4 = [6, 5, 4, 3, 2, 1]
    selection_sort(a4)
    assert a4 == [1, 2, 3, 4, 5, 6]
