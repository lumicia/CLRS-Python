from src.chap2.binary_search import binary_search
from src.chap2.binary_search import binary_search_recursive


def test_binary_search_empty():
    a1 = []
    assert binary_search(a1, 0, 0, 0) == None


def test_binary_search_one_element():
    a2 = [1]
    assert binary_search(a2, 1, 0, 0) == 0


def test_binary_search_case_one():
    a3 = [3, 5, 7, 8, 9, 12]
    assert binary_search(a3, 8, 0, 5) == 3


def test_binary_search_case_two():
    a4 = [2, 5, 9, 12, 16]
    binary_search(a4, 12, 0, 5)
    assert binary_search(a4, 12, 0, 4) == 3


def test_binary_search_recursive_empty():
    a1 = []
    assert binary_search_recursive(a1, 0, 0, 0) == None


def test_binary_search_recursive_one_element():
    a2 = [1]
    assert binary_search_recursive(a2, 1, 0, 0) == 0


def test_binary_search_recursive_case_one():
    a3 = [3, 5, 7, 8, 9, 12]
    assert binary_search_recursive(a3, 8, 0, 5) == 3


def test_binary_search_recursive_case_two():
    a4 = [2, 5, 9, 12, 16]
    assert binary_search(a4, 12, 0, 4) == 3
