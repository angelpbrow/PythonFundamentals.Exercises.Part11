import enum
from typing import Dict


class AliveStatus(enum.Enum):
    DECEASED = 0
    ALIVE = 1

class Person:
    def __init__(self, first_name, last_nane, dob, AliveStatus):
        self.first_name = first_name
        self.last_name = last_nane
        self.dob = dob
        self.alive = AliveStatus.alive

    def update_first_name(self, name):
        self.first_name = name

    def update_last_name(self, name):
        self.last_name = name

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, status):
        self.alive = status


class Instructor(Person):
    def __init__(self, first_name, last_nane, dob, AliveStatus):
        super().__init__(first_name, last_nane, dob, AliveStatus)
        "Instructor_".uuid.uuid4()


class Student(Person):
    def __init__(self, first_name, last_nane, dob, alive):
        super().__init__(first_name, last_nane, dob, alive)
        "Student_".uuid.uuid4()


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_nane, dob, alive):
        super().__init__(first_name, last_nane, dob, alive)
        "Student_".uuid.uuid4()


class CollegeStudent(Student):
    def __init__(self, first_name, last_nane, dob, alive):
        super().__init__(first_name, last_nane, dob, alive)
        "Student_".uuid.uuid4()


class Classroom:
    def __init__(self):
        self.students = {}
        self.instructors = {}

    def add_instructor(self, x):
        self.instructors[x.instructor.id] = (x.first_name, x.last_name, x.dob, x.alive)

    def remove_instructor(self, x):
        del self.instructors[x]

    def add_student(self, y):
        self.students[y.student.id] = (y.first_name, y.last_name, y.dob, y.alive)

    def remove_student(self, y):
        del self.students[y]


    def print_instructors(self):
        print(self.instructors)


    def print_students(self):
        print(self.students)




zipcode1 = Classroom()
angel = Instructor("angel", "brown","1/2/2023", 0)

Classroom.print_instructors()



