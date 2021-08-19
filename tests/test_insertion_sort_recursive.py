from src.chap2.insertion_sort_recursive import insertion_sort_recursive


def test_insertion_sort_recursive_empty():
    a1 = []
    insertion_sort_recursive(a1, 0)
    assert a1 == []


def test_insertion_sort_recursive_one_element():
    a2 = [1]
    insertion_sort_recursive(a2, 0)
    assert a2 == [1]


def test_insertion_sort_recursive_reversed():
    a3 = [6, 5, 4, 3, 2, 1]
    insertion_sort_recursive(a3, 5)
    assert a3 == [1, 2, 3, 4, 5, 6]


def test_insertion_sort_recursive_case_one():
    a1 = [3, 8, 5, 2, 1, 9]
    insertion_sort_recursive(a1, 5)
    assert a1 == [1, 2, 3, 5, 8, 9]
