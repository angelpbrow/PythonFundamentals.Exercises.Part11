import enum

class AliveStatus(enum.Enum):
    DECEASED = 0
    ALIVE = 1

class Person:
    def __init__(self, first_name, last_nane, dob, alive):
        self.first_name = first_name
        self.last_name = last_nane
        self.dob = dob
        self.alive = alive

    def update_first_name(self):
        pass

    def update_last_name(self):
        pass

    def update_dob(self):
        pass

    def update_status(self):
        pass


class Instructor(Person):
    def __init__(self, first_name, last_nane, dob, alive, instructor_id):
        super().__init__(first_name, last_nane, dob, alive)
        "Instructor_".uuid.uuid4()


class Student(Person):
    def __init__(self, first_name, last_nane, dob, alive, student_id):
        super().__init__(first_name, last_nane, dob, alive)
        "Student_".uuid.uuid4()


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_nane, dob, alive, student_id):
        super().__init__(first_name, last_nane, dob, alive)
        "Student_".uuid.uuid4()


class CollegeStudent(Student):
    def __init__(self, first_name, last_nane, dob, alive, student_id):
        super().__init__(first_name, last_nane, dob, alive)
        "Student_".uuid.uuid4()


class Classroom:
    def __init__(self):
        self.students: Dict[str, Person] = dict()
        self.instructors: Dict[str, Person] = dict()






