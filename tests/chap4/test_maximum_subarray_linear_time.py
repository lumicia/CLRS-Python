from src.chap4.exercises.exercise_4_1_5_maximum_subarray_linear_time import (
    maximum_subarray_dp,
    maximum_subarray_dp2,
    maximum_subarray_greedy,
    maximum_subarray_kadane,
)


# Dynamic Programming using a list to store the maximum subarray
def test_maximum_subarray_dp_linear_time_one_element():
    a = [1]
    assert maximum_subarray_dp(a) == (0, 0, 1)


def test_maximum_subarray_dp_linear_time_case_one():
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    assert maximum_subarray_dp(a) == (7, 10, 43)


def test_maximum_subarray_dp_linear_time_case_two():
    a = [1, -4, 3, -4]
    assert maximum_subarray_dp(a) == (2, 2, 3)


def test_maximum_subarray_dp_linear_time_case_three():
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert maximum_subarray_dp(a) == (3, 6, 6)


# Dynamic Programming using a single variable to store the maximum subarray
def test_maximum_subarray_dp2_linear_time_one_element():
    a = [1]
    assert maximum_subarray_dp2(a) == (0, 0, 1)


def test_maximum_subarray_dp2_linear_time_case_one():
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    assert maximum_subarray_dp2(a) == (7, 10, 43)


def test_maximum_subarray_dp2_linear_time_case_two():
    a = [1, -4, 3, -4]
    assert maximum_subarray_dp2(a) == (2, 2, 3)


def test_maximum_subarray_dp2_linear_time_case_three():
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert maximum_subarray_dp2(a) == (3, 6, 6)


# Kadane's algorithm
def test_maximum_subarray_kadane_linear_time_one_element():
    a = [1]
    assert maximum_subarray_kadane(a) == (0, 0, 1)


def test_maximum_subarray_kadane_linear_time_case_one():
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    assert maximum_subarray_kadane(a) == (7, 10, 43)


def test_maximum_subarray_kadane_linear_time_case_two():
    a = [1, -4, 3, -4]
    assert maximum_subarray_kadane(a) == (2, 2, 3)


def test_maximum_subarray_kadane_linear_time_case_three():
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert maximum_subarray_kadane(a) == (3, 6, 6)


# Greedy
def test_maximum_subarray_greedy_linear_time_one_element():
    a = [1]
    assert maximum_subarray_greedy(a) == (0, 0, 1)


def test_maximum_subarray_greedy_linear_time_case_one():
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    assert maximum_subarray_greedy(a) == (7, 10, 43)


def test_maximum_subarray_greedy_linear_time_case_two():
    a = [1, -4, 3, -4]
    assert maximum_subarray_greedy(a) == (2, 2, 3)


def test_maximum_subarray_greedy_linear_time_case_three():
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert maximum_subarray_greedy(a) == (3, 6, 6)
