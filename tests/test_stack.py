from src.chap10.stack import Stack
def test_empty_stack():
    s1=Stack(0)
    assert s1.is_empty()==True
def test_one_element_stack():
    s2=Stack(1)
    s2.push(10)
    assert s2.is_empty()==False
    assert s2.pop()==10
def test_stack_case_one():
    s3=Stack(3)
    assert s3.is_empty()== True
    s3.push(1)
    s3.push(5)
    s3.push(9)
    assert s3.is_full()==True
    assert s3.pop()==9