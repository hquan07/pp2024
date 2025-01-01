import math
import numpy as np
from rich.console import Console
from rich.table import Table

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

class ManagementSystem:
    def __init__(self):
        self._students = []
        self._courses = []

    def input_students(self):
        num_students = self._input_positive_integer("Enter the number of students: ")
        for _ in range(num_students):
            student = self._input_student_info()
            self._students.append(student)

    def input_courses(self):
        num_courses = self._input_positive_integer("Enter the number of courses: ")
        for _ in range(num_courses):
            course = self._input_course_info()
            self._courses.append(course)

    def input_marks(self):
        course_id = input("Enter Course ID to input marks: ")
        course = self._find_course(course_id)
        if not course:
            print("Course not found.")
            return

        for student in self._students:
            mark = float(input(f"Enter marks for {student.get_name()}: "))
            student.add_mark(course_id, mark)

    def calculate_gpas(self):
        course_credits = {course.get_id(): course.get_credit() for course in self._courses}
        for student in self._students:
            student.calculate_gpa(course_credits)

    def sort_students_by_gpa(self):
        self._students = sorted(self._students, key=lambda s: s.get_gpa(), reverse=True)

    def display_students_with_rich(self):
        console = Console()
        table = Table(title="Student List", show_header=True, header_style="bold magenta")
        table.add_column("ID", justify="center")
        table.add_column("Name", justify="left")
        table.add_column("DOB", justify="center")
        table.add_column("GPA", justify="center")
        table.add_column("Marks", justify="left")

        for student in self._students:
            table.add_row(
                str(student.get_id()),
                student.get_name(),
                student.get_dob(),
                str(student.get_gpa()),
                str(student._marks)
            )

        console.print(table)

    def _input_positive_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def _input_student_info(self):
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Student DOB (YYYY-MM-DD): ")
        return Student(id, name, dob)

    def _input_course_info(self):
        id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        credit = int(input("Enter Course Credit: "))
        return Course(id, name, credit)

    def _find_course(self, course_id):
        for course in self._courses:
            if course.get_id() == course_id:
                return course
        return None

def main():
    system = ManagementSystem()
    system.input_courses()
    system.input_students()
    system.input_marks()
    system.calculate_gpas()
    system.sort_students_by_gpa()
    system.display_students_with_rich()

if __name__ == "__main__":
    main()
