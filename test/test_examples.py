"""test_examples.py - tests for examples.py
"""
import pytest

from examples import power2
from examples import fibo


def test_power2():
    assert power2(0) == 1
    assert power2(1) == 2
    assert power2(2) == 4

"""
@pytest.mark.parametrize('n,expected', [
    (1,1),
    (2,1),
    (3,2),
    (4,3),
    (5,5),
    (6,8)
])

def test_fibo(n, expected):
    assert fibo(n) == expected
"""

@pytest.mark.parametrize('n,expected', [
    (1,1),
    (2,1),
    (7,13),
    ...
    (8,21),
    (0, RuntimeError),
    (-1, RuntimeError)
])
def test_fibo(n,expected):
    if isinstance(expected,type) and issubclass(expected,Exception):
        with pytest.raises(expected):
            fibo(n)
    else:
        assert fibo(n) == expected