# Pobierz z pliku tekstowego listę osób i wypisz te osoby, które
# są pełnoletnie.

from dataclasses import dataclass
from typing import Self, Any, Callable
import re

@dataclass
class Person:
    id_: int
    name: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 18

    @classmethod
    def from_text(cls, person_text: str) -> Self:
        # 5;KAMIL;35
        if not re.match(r'^\d+;[A-Z]+;\d+$', person_text):
            raise ValueError('Person text is not correct')

        items = person_text.split(';')
        return cls(int(items[0]), items[1], int(items[2]))

class TextFileReader:
    @staticmethod
    def read(filename: str, converter_fn: Callable[[str], Any]) -> Any:
        with open(filename) as f:
            return [
                converter_fn(line[:-1] if line[-1] == '\n' else line)
                for line in f.readlines()
            ]

@dataclass
class PeopleService:
    people: list[Person]

    def get_adult_people(self) -> list[Person]:
        return [person for person in self.people if person.is_adult()]


def main() -> None:
    people = TextFileReader.read(
        'people.txt',
        lambda line: Person.from_text(line))
    print(people)

    people_service = PeopleService(people)
    print(people_service.get_adult_people())

if __name__ == '__main__':
    main()