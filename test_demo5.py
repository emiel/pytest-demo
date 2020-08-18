from dataclasses import dataclass
from unittest import mock

import pytest

from demo5 import random_greet

# app/library code


@dataclass
class Person:
    name: str


# test code


@pytest.fixture
def alice():
    return Person(name="Alice")


@mock.patch("demo5.choice", autospec=True, return_value="Hello")
def test_random_greet(mock_random_greet, alice):
    # Act
    greeting = random_greet(alice)

    # Assert
    assert greeting == "Hello Alice"

    mock_random_greet.assert_called_once()
