from dataclasses import dataclass

import pytest

# app/library code


@dataclass
class Person:
    name: str


def greet(person):
    return f"Hello {person.name}"


# test code


@pytest.fixture
def alice():
    return Person(name="Alice")


def test_greet(alice):
    # Act
    greeting = greet(alice)

    # Assert
    assert greeting == "Hello Alice"
