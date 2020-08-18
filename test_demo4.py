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
def make_person(**kwargs):
    def _make_person(**kwargs):
        return Person(**kwargs)

    return _make_person


def test_greet(make_person):
    # Arrange
    people = [make_person(name="Alice"), make_person(name="Bob")]

    # Act
    greetings = [greet(person) for person in people]

    # Assert
    assert greetings == ["Hello Alice", "Hello Bob"]
