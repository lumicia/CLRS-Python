from src.chap2.exercises.problem2_4_inversion import inversion_count


def test_inversions_empty():
    a1 = []
    assert inversion_count(a1, 0, 0) == 0


def test_inversions_one_element():
    a2 = [1]
    assert inversion_count(a2, 0, 0) == 0


def test_inversions_case_one():
    a3 = [2, 3, 8, 6, 1]
    assert inversion_count(a3, 0, 4) == 5
