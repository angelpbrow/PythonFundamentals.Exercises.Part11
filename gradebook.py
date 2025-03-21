import enum
import uuid


class AliveStatus(enum.Enum):
    DECEASED = 0
    ALIVE = 1

class Person:
    def __init__(self, first_name, last_nane, dob, AliveStatus):
        self.first_name = first_name
        self.last_name = last_nane
        self.dob = dob
        self.alive = AliveStatus.ALIVE

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
        self.instructor_id = ("Instructor_" + str(uuid.uuid4()))


class Student(Person):
    def __init__(self, first_name, last_nane, dob, AliveStatus):
        super().__init__(first_name, last_nane, dob, AliveStatus)
        self.student_id = ("Student_" + str(uuid.uuid4()))


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_nane, dob, AliveStatus):
        super().__init__(first_name, last_nane, dob, AliveStatus)
        self.student_id = ("Student_" + str(uuid.uuid4()))


class CollegeStudent(Student):
    def __init__(self, first_name, last_nane, dob, AliveStatus):
        super().__init__(first_name, last_nane, dob, AliveStatus)
        self.student_id = ("Student_" + str(uuid.uuid4()))


class Classroom:
    def __init__(self):
        self.students = {}
        self.instructors = {}

    def add_instructor(self, x):
        self.instructors[x.instructor_id] = (x.first_name, x.last_name, x.dob, x.alive)

    def remove_instructor(self, z):
        del self.instructors[z]

    def add_student(self, y):
        self.students[y.student_id] = (y.first_name, y.last_name, y.dob, y.alive)

    def remove_student(self, z):
        del self.students[z]


    def print_instructors(self):
        print(self.instructors)


    def print_students(self):
        print(self.students)



angel = Instructor("angel", "brown","1/2/2023", AliveStatus.ALIVE)
jim = Instructor("jim","heller","3/12/2019", AliveStatus.ALIVE)
print(angel.instructor_id)
print(jim.instructor_id)

zipcode1 = Classroom()
zipcode1.add_instructor(jim)
zipcode1.add_instructor(angel)
zipcode1.print_instructors()





