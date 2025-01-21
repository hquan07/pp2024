import tkinter as tk
from tkinter import messagebox
from domains.management_system import ManagementSystem, Student, Course
from input import get_input

class ManagementSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Management System")
        self.system = ManagementSystem()

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.course_button = tk.Button(self.frame, text="Input Courses", command=self.input_courses)
        self.course_button.grid(row=0, column=0, padx=5, pady=5)

        self.student_button = tk.Button(self.frame, text="Input Students", command=self.input_students)
        self.student_button.grid(row=0, column=1, padx=5, pady=5)

        self.marks_button = tk.Button(self.frame, text="Input Marks", command=self.input_marks)
        self.marks_button.grid(row=0, column=2, padx=5, pady=5)

        self.calculate_gpa_button = tk.Button(self.frame, text="Calculate GPAs", command=self.calculate_gpas)
        self.calculate_gpa_button.grid(row=1, column=0, padx=5, pady=5)

        self.sort_button = tk.Button(self.frame, text="Sort Students by GPA", command=self.sort_students_by_gpa)
        self.sort_button.grid(row=1, column=1, padx=5, pady=5)

        self.display_button = tk.Button(self.frame, text="Display Students", command=self.display_students)
        self.display_button.grid(row=1, column=2, padx=5, pady=5)

    def input_courses(self):
        num_courses = self.get_input("Enter the number of courses:", int)
        for _ in range(num_courses):
            id = self.get_input("Enter Course ID:", str)
            name = self.get_input("Enter Course Name:", str)
            credit = self.get_input("Enter Course Credit:", int)
            self.system._courses.append(Course(id, name, credit))
        self.system.save_courses()

    def input_students(self):
        num_students = self.get_input("Enter the number of students:", int)
        for _ in range(num_students):
            id = self.get_input("Enter Student ID:", str)
            name = self.get_input("Enter Student Name:", str)
            dob = self.get_input("Enter Student DOB (YYYY-MM-DD):", str)
            self.system._students.append(Student(id, name, dob))
        self.system.save_students()

    def input_marks(self):
        course_id = self.get_input("Enter Course ID to input marks:", str)
        course = next((c for c in self.system._courses if c.get_id() == course_id), None)
        if not course:
            messagebox.showerror("Error", "Course not found.")
            return

        for student in self.system._students:
            mark = self.get_input(f"Enter marks for {student.get_name()}:", float)
            student.add_mark(course_id, mark)
        self.system.save_marks()

    def calculate_gpas(self):
        self.system.calculate_gpas()
        messagebox.showinfo("Info", "GPAs calculated successfully.")

    def sort_students_by_gpa(self):
        self.system.sort_students_by_gpa()
        messagebox.showinfo("Info", "Students sorted by GPA successfully.")

    def display_students(self):
        self.system.display_students_with_rich()

    def get_input(self, prompt, cast_func):
        input_window = tk.Toplevel(self.root)
        input_window.title("Input")

        tk.Label(input_window, text=prompt).pack(padx=10, pady=10)
        input_entry = tk.Entry(input_window)
        input_entry.pack(padx=10, pady=10)
        input_value = []

        def on_submit():
            try:
                value = cast_func(input_entry.get())
                input_value.append(value)  # Store value in a list to capture it
                input_window.destroy()
            except ValueError:
                messagebox.showerror("Error", f"Invalid input. Please enter a valid {cast_func.__name__}.")

        submit_button = tk.Button(input_window, text="Submit", command=on_submit)
        submit_button.pack(padx=10, pady=10)

        self.root.wait_window(input_window)
        return input_value[0] if input_value else None

def main():
    root = tk.Tk()
    app = ManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
