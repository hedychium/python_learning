# encoding=utf-8

"""
__project_ = 'py-worksapce'
__file_name__ = 'test_sample'
__author__ = 'li.jiang'
__time__ = '2019/8/22 16:50'
__product_name = PyCharm
# Keep calm and carry on 
"""
import pytest
def reverse(string):
    return string[::-1]

def test_reverse():
    string = "good"
    assert reverse(string) == "doog"

    another_string = "itest"
    # assert reverse(another_string) == "tse55ti"


@pytest.mark.p0
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        # f()
    print(str(excinfo.value))
    assert 'maximum recursion' in str(excinfo.value)

test_recursion_depth()
