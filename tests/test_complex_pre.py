import pytest
import contrapy
import math


def test_single_complex_check():
    def sum_is_10(a, b, c):
        return a + b + c == 10

    @contrapy.check(sum_is_10)
    def demo(a, b, c):
        return True

    with pytest.raises(ValueError):
        demo(5, 5, 5)

    assert demo(4, 4, 2)


def test_multiple_complex_checks():
    def sum_is_10(a, b, c):
        return a + b + c == 10

    def prod_is_zero(a, b, c):
        return a * b * c == 0

    @contrapy.check(sum_is_10, prod_is_zero)
    def demo(a, b, c):
        return True

    with pytest.raises(ValueError):
        demo(4, 4, 2)

    assert demo(5, 5, 0)


def test_argument_complex_combined():
    def sum_is_10(a, b, c):
        return a + b + c == 10

    def prod_is_zero(a, b, c):
        return a * b * c == 0

    @contrapy.check(sum_is_10, prod_is_zero)
    def demo(a : int, b : int, c : int) -> bool:
        return True

    with pytest.raises(ValueError):
        demo(4, 4, 2)

    with pytest.raises(TypeError):
        demo(5, 5, 0.0)

    assert demo(5, 5, 0)
