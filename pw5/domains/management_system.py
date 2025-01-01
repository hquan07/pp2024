from .student import Student
from .course import Course
from rich.console import Console
from rich.table import Table
import os
import zipfile

class ManagementSystem:
    def __init__(self):
        self._students = []
        self._courses = []
        self.load_data()
        
    def load_data(self):
        if os.path.exists("student.dat"):
            with zipfile.Zipfile("Student.dat", "r") as zip_ref:
                zip_ref.extractall()
            self.load_students()
            self.load_courses()
            self.load_marks()
            
    def load_students(self):
        if os.path.exists("Student.txt"):
            with open("Student.txt", "r") as file:
                for line in file:
                    id, name, dob = line.strip().split(", ")
                    self._students.append(Student(id, name, dob))
                    
    def load_course(self):
        if os.path.exists("course.txt"):
            with open("course.txt", "r") as file:
                for line in file:
                    id , name, credit = line.strip().split(", ")
                    self.courses.append(Course(id, name, int(credit)))
                    
    def load_marks(self):
        if os.path.exists("marks.txt"):
            with open("marks.txt", "r") as file:
                for line in file:
                    student_id, course_id, mark = line.strip().split(", ")
                    student = next((s for s in self._students if s.get_id()== student_id), None)
                    if student:
                        student.add_mark(course_id, float(mark))

    def input_students(self, input_func):
        num_students = input_func("Enter the number of students: ", int)
        with open("Student.txt", "w") as file:
         for _ in range(num_students):
            id = input_func("Enter Student ID: ", str)
            name = input_func("Enter Student Name: ", str)
            dob = input_func("Enter Student DOB (YYYY-MM-DD): ", str)
            self._students.append(Student(id, name, dob))
            file.write(f"{id}, {name}, {dob}\n")

    def input_courses(self, input_func):
        num_courses = input_func("Enter the number of courses: ", int)
        with open("course.txt", "w") as file:
         for _ in range(num_courses): 
            id = input_func("Enter Course ID: ", str)
            name = input_func("Enter Course Name: ", str)
            credit = input_func("Enter Course Credit: ", int)
            self._courses.append(Course(id, name, credit))
            file.write(f"{id}, {name}, {credit}\n")

    def input_marks(self, input_func):
        course_id = input("Enter Course ID to input marks: ")
        course = next((c for c in self._courses if c.get_id() == course_id), None)
        if not course:
            print("Course not found.")
            return
        with open("marks.txt", "w") as file:
         for student in self._students:
            mark = input_func(f"Enter marks for {student.get_name()}: ", float)
            student.add_mark(course_id, mark)
            file.write(f"{student.get_id()}, {course_id}, {mark}\n")

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
        
    def compress_data(self):
        with zipfile.Zipfile("student.dat", "w") as zipf:
            zipf.write("student.txt")
            zipf.write("Course.txt")
            zipf("Marks.txt")
            
    def __del__(self):
        self.compress_data()
        
