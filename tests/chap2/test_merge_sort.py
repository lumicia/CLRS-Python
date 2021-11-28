from typing import Union

from src.chap2.merge_sort import merge_sort


def test_merge_sort_with_sentinels_empty():
    a1 = []
    merge_sort(a1, 0, 0)
    assert a1 == []


def test_merge_sort_with_sentinels_one_element():
    a2: list[Union[int, float]] = [1]
    merge_sort(a2, 0, 0)
    assert a2 == [1]


def test_merge_sort_with_sentinels_reversed():
    a3: list[Union[int, float]] = [6, 5, 4, 3, 2, 1]
    merge_sort(a3, 0, 5)
    assert a3 == [1, 2, 3, 4, 5, 6]


def test_merge_sort_with_sentinels_case_one():
    a4: list[Union[int, float]] = [2, 4, 5, 7, 1, 2, 3, 6]
    merge_sort(a4, 0, 7)
    assert a4 == [1, 2, 2, 3, 4, 5, 6, 7]
