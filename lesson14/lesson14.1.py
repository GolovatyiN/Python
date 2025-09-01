class GroupLimitError(Exception):

    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} років'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Студент: {self.first_name} {self.last_name}, {self.gender}, {self.age} років, залікова книжка: {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Група: {self.number}\n{all_students}'

gr = Group("PD1")

for i in range(10):
    gr.add_student(Student("Male", 20+i, f"Name{i}", f"Surname{i}", f"RB{i}"))

print("✅ Додано 10 студентів успішно")

try:
    gr.add_student(Student("Female", 22, "Extra", "Student", "RBX"))
except GroupLimitError as e:
    print("⛔ Помилка:", e)