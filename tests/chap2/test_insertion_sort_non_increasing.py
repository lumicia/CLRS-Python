from src.chap2.exercises.exercise2_1_2_insertion_sort_non_decreasing import (
    insertion_sort_non_decreasing,
)


def test_insertion_sort_non_decreasing_empty():
    a1 = []
    insertion_sort_non_decreasing(a1)
    assert a1 == []


def test_insertion_sort_non_decreasing_one_element():
    a2 = [1]
    insertion_sort_non_decreasing(a2)
    assert a2 == [1]


def test_insertion_sort_non_decreasing_case_one():
    a3 = [5, 2, 4, 6, 1, 3]
    insertion_sort_non_decreasing(a3)
    assert a3 == [6, 5, 4, 3, 2, 1]


def test_insertion_sort_non_decreasing_case_two():
    a4 = [5, 5, 3, 6, 2, 1]
    insertion_sort_non_decreasing(a4)
    assert a4 == [6, 5, 5, 3, 2, 1]


def test_insertion_sort_non_decreasing_reversed():
    a5 = [6, 5, 4, 3, 2, 1]
    insertion_sort_non_decreasing(a5)
    assert a5 == [6, 5, 4, 3, 2, 1]
