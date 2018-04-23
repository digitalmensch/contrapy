import pytest
import contrapy


def test_argument_type_bool():

    @contrapy.check()
    def demo(a: True):
        return True

    with pytest.raises(ValueError):
        demo(False)

    assert demo(True)


def test_argument_type_int():

    @contrapy.check()
    def demo(a: 42):
        return True

    with pytest.raises(ValueError):
        demo(123)

    assert demo(42)


def test_argument_type_float():

    @contrapy.check()
    def demo(a: 3.14):
        return True

    with pytest.raises(ValueError):
        demo(6.28)

    assert demo(3.14)


def test_argument_type_str():

    @contrapy.check()
    def demo(a: "hello"):
        return True

    with pytest.raises(ValueError):
        demo("not hello")

    assert demo("hello")
