from src.chap2.horner_rule import naive_polynomial_evaluation
from src.chap2.horner_rule import horner_rule


def test_naive_polynomial_evaluation_empty():
    a1 = []
    assert naive_polynomial_evaluation(a1, 0) == 0


def test_naive_polynomial_evaluation_case_one():
    a2 = [2, 3]
    assert naive_polynomial_evaluation(a2, 2) == 8


def test_naive_polynomial_evaluation_case_two():
    a3 = [5, 3, 6, 9, 1]
    assert naive_polynomial_evaluation(a3, 3) == 392


def test_horner_rule_empty():
    a1 = []
    assert horner_rule(a1, 0) == 0


def test_horner_rule_case_one():
    a2 = [2, 3]
    assert horner_rule(a2, 2) == 8


def test_horner_rule_case_two():
    a3 = [5, 3, 6, 9, 1]
    assert horner_rule(a3, 3) == 392
