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


