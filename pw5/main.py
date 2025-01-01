from domains.management_system import ManagementSystem
from input import get_input

def main():
    system = ManagementSystem()
    system.input_courses(get_input)
    system.input_students(get_input)
    system.input_marks(get_input)
    system.calculate_gpas()
    system.sort_students_by_gpa()
    system.display_students_with_rich()
    
if __name__ == "__main__":
    main()

    