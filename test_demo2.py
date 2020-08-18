from dataclasses import dataclass

# app/library code


@dataclass
class Person:
    name: str


def greet(person):
    return f"Hello {person.name}"


# test code


def test_greet():
    # Arrange
    alice = Person(name="Alice")

    # Act
    greeting = greet(alice)

    # Assert
    assert greeting == "Hello Alice"
