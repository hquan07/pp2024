class Student:
    def __init__(self, id, name, dob, marks={}):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = marks

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Input function
def input_num_students():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            return num_students
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_student_info():
    while True:
        try:
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            dob = input("Enter student DOB (YYYY-MM-DD): ")
            return Student(id, name, dob)
        except ValueError:
            print("Invalid input. Please enter valid ID and date format (YYYY-MM-DD).")

# Listing functions
def list_courses(courses):
    for course in courses:
        print(f"Course ID: {course.id}, Course Name: {course.name}")

def list_students(students):
    for student in students:
        print(f"Student ID: {student.id}, Name: {student.name}, DOB: {student.dob}")

def show_student_marks(students, course_id):
    for student in students:
        if course_id in student.marks:
            print(f"Student ID: {student.id}, Name: {student.name}, Marks: {student.marks[course_id]}")
        else:
            print(f"Student ID: {student.id}, Name: {student.name}, Course not found.")

# Main function
def main():
    num_students = input_num_students()
    students = [input_student_info() for _ in range(num_students)]

if __name__ == "__main__":
    main()