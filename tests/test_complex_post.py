import pytest
import contrapy
import math


def test_argument_complex_combined():
    def sum_is_10(a, b, c):
        return a + b + c == 10

    def prod_is_zero(a, b, c):
        return a * b * c == 0

    def this_combination(a, b, c, _return):
        return a == 5 and b == 5 and c == 0 and _return == 1

    @contrapy.check(sum_is_10, prod_is_zero, this_combination)
    def good(a : int, b : int, c : int) -> 1:
        return (a + b) ** c

    @contrapy.check(sum_is_10, prod_is_zero, this_combination)
    def bad(a : int, b : int, c : int):
        return 999

    with pytest.raises(ValueError):
        good(4, 4, 2)

    with pytest.raises(TypeError):
        good(5, 5, 0.0)

    with pytest.raises(ValueError):
        bad(5, 5, 0)

    assert 1 == good(5, 5, 0)
