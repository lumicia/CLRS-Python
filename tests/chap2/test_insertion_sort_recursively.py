from src.chap2.exercises.exercise2_3_4_insertion_sort_recursively import insertion_sort


def test_insertion_sort_recursively_empty():
    a1 = []
    insertion_sort(a1, 0)
    assert a1 == []


def test_insertion_sort_recursively_one_element():
    a2 = [1]
    insertion_sort(a2, 0)
    assert a2 == [1]


def test_insertion_sort_recursively_reversed():
    a3 = [6, 5, 4, 3, 2, 1]
    insertion_sort(a3, 5)
    assert a3 == [1, 2, 3, 4, 5, 6]


def test_insertion_sort_recursively_case_one():
    a1 = [3, 8, 5, 2, 1, 9]
    insertion_sort(a1, 5)
    assert a1 == [1, 2, 3, 5, 8, 9]
