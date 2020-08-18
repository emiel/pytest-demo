import pytest

# app/library code


def add(x, y):
    return x + y


# test code


def test_add():
    assert add(1, 2) == 3


@pytest.mark.skip("buggy code here")
def test_add_fail():
    assert add(1, 2) == 5
