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

    def add_mark(self, course_id, mark):
        self._marks[course_id] = mark

    def get_mark(self, course_id):
        return self._marks.get(course_id, None)

    def display(self):
        base_info = super().display()
        return f"{base_info}, Marks: {self._marks}"


class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def display(self):
        return f"Course ID: {self._id}, Course Name: {self._name}"


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

    def list_students(self):
        print("Listing Students:")
        for student in self._students:
            print(student.display())

    def list_courses(self):
        print("Listing Courses:")
        for course in self._courses:
            print(course.display())

    def input_marks(self):
        course_id = input("Enter Course ID to input marks: ")
        course = self._find_course(course_id)
        if not course:
            print("Course not found.")
            return

        for student in self._students:
            mark = self._input_positive_integer(f"Enter marks for {student.get_name()}: ")
            student.add_mark(course_id, mark)

    def show_student_marks(self):
        course_id = input("Enter Course ID to view marks: ")
        course = self._find_course(course_id)
        if not course:
            print("Course not found.")
            return

        print(f"Marks for Course: {course.get_name()} ({course_id})")
        for student in self._students:
            mark = student.get_mark(course_id)
            if mark is not None:
                print(f"{student.get_name()}: {mark}")
            else:
                print(f"{student.get_name()}: No marks available.")

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
        while True:
            try:
                id = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                dob = input("Enter Student DOB (YYYY-MM-DD): ")
                return Student(id, name, dob)
            except ValueError:
                print("Invalid input. Try again!")

    def _input_course_info(self):
        id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        return Course(id, name)

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
    system.list_courses()
    system.list_students()
    system.show_student_marks()


if __name__ == "__main__":
    main()
