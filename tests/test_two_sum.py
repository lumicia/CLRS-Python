from src.chap2.two_sum import two_sum


def test_two_sum_case_one():
    a1 = [1, 2]
    assert two_sum(a1, 3) == [0, 1]


def test_wo_sum_case_two():
    a2 = [1, 3, 6, 7, 9]
    assert two_sum(a2, 9) == [1, 2]


def test_wo_sum_case_three():
    a3 = [1, 2, 3, 7, 8, 9]
    assert two_sum(a3, 7) == [None, None]
