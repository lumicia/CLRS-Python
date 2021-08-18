from src.chap2.linear_search import linear_search


def test_linear_search_empty():
    a1 = []
    assert linear_search(a1, 1) == None


def test_linear_search_one_element():
    a2 = [1]
    assert linear_search(a2, 1) == 0


def test_linear_search_none_element():
    a3 = [None, None, None]
    assert linear_search(a3, 1) == None


def test_linear_search_case_one():
    a4 = [1, 2, 3, 4, 5]
    assert linear_search(a4, 3) == 2
