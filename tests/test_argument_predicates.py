import pytest
import contrapy
import math


def test_argument_lambda():

    @contrapy.check()
    def demo(a: (lambda a: a > 10)):
        return True

    with pytest.raises(ValueError):
        demo(5)

    assert demo(11)


def test_argument_named():

    def is_multiple_of_pi(val):
        return val % math.pi == 0

    good = math.pi * 7
    bad = good + 1

    @contrapy.check()
    def demo(a: is_multiple_of_pi):
        return True

    with pytest.raises(ValueError):
        demo(bad)

    assert demo(good)
