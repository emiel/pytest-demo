from random import choice

greetings = [
    "Bună ziua",
    "Bonjour",
    "Guten tag",
    "אַ גוטן טאָג",
    "Goede dag",
    "God dag",
]


def random_greet(person):
    greeting = choice(greetings)
    return f"{greeting} {person.name}"
