from src.chap4.exercises.exercise_4_1_2_maximum_subarray_brute_force import maximum_subarray
def test_maximum_subarray_brute_force_one_element():
    a=[1]
    assert maximum_subarray(a)==(0,0,1)
def test_maximum_subarray_brute_force_case_one():
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    assert maximum_subarray(a) == (7, 10, 43)

def test_maximum_subarray_case_two():
    a = [1, -4, 3, -4]
    assert maximum_subarray(a) == (2, 2, 3)


