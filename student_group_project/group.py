from typing import Optional, Set
from models.student import Student
from models.exceptions import GroupLimitError

class Group:
    MAX_SIZE = 10

    def __init__(self, number: str):
        self.number = number
        self.group: Set[Student] = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= self.MAX_SIZE:
            raise GroupLimitError("У групі не може бути більше 10 студентів!")
        self.group.add(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        for st in self.group:
            if st.last_name == last_name:
                return st
        return None

    def delete_student(self, last_name: str) -> None:
        st = self.find_student(last_name)
        if st is not None:
            self.group.remove(st)

    def __str__(self) -> str:
        all_students = "\n".join(str(st) for st in sorted(self.group, key=lambda s: (s.last_name, s.first_name)))
        return f"Група: {self.number}\n{all_students}"
