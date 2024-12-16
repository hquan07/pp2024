class Course:
    def __init__(self, id, name, credit):
        self._id = id
        self._name = name
        self._credit = credit

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_credit(self):
        return self._credit

    def display(self):
        return f"Course ID: {self._id}, Course Name: {self._name}, Credit: {self._credit}"
