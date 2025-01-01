from .person import Person
import math

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        self._marks = {}
        self._gpa = 0.0

    def add_mark(self, course_id, mark):
        self._marks[course_id] = math.floor(mark * 10) / 10

    def get_mark(self, course_id):
        return self._marks.get(course_id, None)

    def calculate_gpa(self, course_credits):
        total_credits = sum(course_credits.values())
        weighted_sum = sum(self._marks[course_id] * course_credits[course_id] for course_id in self._marks if course_id in course_credits)
        self._gpa = round(weighted_sum / total_credits, 2) if total_credits > 0 else 0.0

    def get_gpa(self):
        return self._gpa

    def display(self):
        base_info = super().display()
        return f"{base_info}, GPA: {self._gpa}, Marks: {self._marks}"
