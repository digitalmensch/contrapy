import pytest
import contrapy


def test_argument_type_bool():
    @contrapy.check()
    def demo(a : bool):
        return True

    with pytest.raises(TypeError):
        demo('not-a-bool')

    assert demo(False)
    assert demo(True)


def test_argument_type_int():
    @contrapy.check()
    def demo(a : int):
        return True


    with pytest.raises(TypeError):
        demo('not-an-int')

    assert demo(123)
    assert demo(0)
    assert demo(-37)


def test_argument_type_float():
    @contrapy.check()
    def demo(a : float):
        return True

    with pytest.raises(TypeError):
        demo('not-a-float')

    assert demo(3.14)
    assert demo(0.0)
    assert demo(-0.4)


def test_argument_type_str():
    @contrapy.check()
    def demo(a : str):
        return True

    with pytest.raises(TypeError):
        demo(0xdeadbeef)

    assert demo('a string')
    assert demo('another str')
