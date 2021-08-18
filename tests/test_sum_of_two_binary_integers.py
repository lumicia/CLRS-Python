from src.chap2.sum_of_two_binary_integers import sum_of_two_binary_intergers


def test_sum_one_bit():
    a = [1]
    b = [1]
    assert sum_of_two_binary_intergers(a, b) == [1, 0]


def test_sum_two_bits():
    a = [1, 0]
    b = [1, 1]
    assert sum_of_two_binary_intergers(a, b) == [1, 0, 1]
