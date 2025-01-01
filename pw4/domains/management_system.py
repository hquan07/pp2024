from .student import Student
from .course import Course
from rich.console import Console
from rich.table import Table

class ManagementSystem:
    def __init__(self):
        self._students = []
        self._courses = []

    def input_students(self, input_func):
        num_students = input_func("Enter the number of students: ", int)
        for _ in range(num_students):
            id = input_func("Enter Student ID: ", str)
            name = input_func("Enter Student Name: ", str)
            dob = input_func("Enter Student DOB (YYYY-MM-DD): ", str)
            self._students.append(Student(id, name, dob))

    def input_courses(self, input_func):
        num_courses = input_func("Enter the number of courses: ", int)
        for _ in range(num_courses):
            id = input_func("Enter Course ID: ", str)
            name = input_func("Enter Course Name: ", str)
            credit = input_func("Enter Course Credit: ", int)
            self._courses.append(Course(id, name, credit))

    def input_marks(self, input_func):
        course_id = input("Enter Course ID to input marks: ")
        course = next((c for c in self._courses if c.get_id() == course_id), None)
        if not course:
            print("Course not found.")
            return

        for student in self._students:
            mark = input_func(f"Enter marks for {student.get_name()}: ", float)
            student.add_mark(course_id, mark)

    def calculate_gpas(self):
        course_credits = {c.get_id(): c.get_credit() for c in self._courses}
        for student in self._students:
            student.calculate_gpa(course_credits)

    def sort_students_by_gpa(self):
        self._students.sort(key=lambda s: s.get_gpa(), reverse=True)

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
                student.get_id(),
                student.get_name(),
                student.get_dob(),
                str(student.get_gpa()),
                str(student._marks)
            )
        console.print(table)
