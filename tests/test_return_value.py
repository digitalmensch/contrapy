import pytest
import contrapy


def test_return_type():
    @contrapy.check()
    def good() -> str:
        return 'some-string'
    @contrapy.check()
    def bad() -> str:
        return 3.14

    with pytest.raises(TypeError):
        bad()

    assert 'some-string' == good()


def test_return_value():
    @contrapy.check()
    def good() -> 0xdeadbeef:
        return 0xdeadbeef
    @contrapy.check()
    def bad() -> 0xdeadbeef:
        return 0xcafebabe

    with pytest.raises(ValueError):
        bad()

    assert 0xdeadbeef == good()


def test_return_lambda():
    @contrapy.check()
    def good() -> (lambda x: x < 10):
        return 7
    @contrapy.check()
    def bad() -> (lambda x: x < 10):
        return 11

    with pytest.raises(ValueError):
        bad()

    assert good() < 10


def test_return_named():
    def str_of_len_7(s):
        return len(s) == 7

    @contrapy.check()
    def good() -> str_of_len_7:
        return '1234567'
    @contrapy.check()
    def bad() -> str_of_len_7:
        return 'some-very-very-long-string'

    with pytest.raises(ValueError):
        bad()

    assert '1234567' == good()
