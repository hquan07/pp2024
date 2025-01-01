class Person:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def display(self):
        return f"ID: {self._id}, Name: {self._name}, DOB: {self._dob}"
