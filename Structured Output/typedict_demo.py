from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


new_person: Person = {
    # hover over 'new_person' to see the type information
    # hover on name or age to see their types
    "name": "Alice",
    "age": 30,
}
