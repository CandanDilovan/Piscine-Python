import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:

    name: str = field(repr=True)
    surname: str = field(repr=True)
    active: bool = field(repr=True)
    login: str = field(repr=True)
    id: str = field(repr=True)

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.active = True
        self.login = "Eagle"
        self.id = generate_id()
