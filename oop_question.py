from typing import List  # Used to specify types for lists (for readability and static analysis)

# Base class for all people in the system
class Person:
    def __init__(self, name: str):
        self.name = name  # Every person has a name

# Institution contains departments and employees
class Institution:
    def __init__(self, name: str):
        self.name = name
        self.departments: List[Department] = []  # List to store Department objects
        self.employees: List[Employee] = []      # List to store Employee objects (faculty, clerks)

    def add_department(self, department):
        self.departments.append(department)  # Adds a department to the list

    def add_employee(self, employee):
        self.employees.append(employee)      # Adds an employee (faculty or clerk) to the list

# A Department contains courses and faculties
class Department:
    def __init__(self, name: str):
        self.name = name
        self.courses: List[Course] = []          # List of Course objects
        self.faculties: List[RegularFaculty] = []  # List of RegularFaculty

    def add_course(self, course):
        self.courses.append(course)              # Adds a course to the department

    def add_faculty(self, faculty):
        self.faculties.append(faculty)           # Adds a regular faculty to the department

# A Course has a title, faculties that teach it, and students who take it
class Course:
    def __init__(self, title: str):
        self.title = title
        self.faculties: List[Faculty] = []       # List of faculties teaching this course
        self.students: List[Student] = []        # List of students enrolled

    def assign_faculty(self, faculty):
        self.faculties.append(faculty)           # Add faculty to course

    def enroll_student(self, student):
        self.students.append(student)            # Add student to course

# Employee is a Person who works at the institution
class Employee(Person):
    def __init__(self, name: str):
        super().__init__(name)                   # Inherit from Person

# Clerk is a type of Employee
class Clerk(Employee):
    def __init__(self, name: str):
        super().__init__(name)

# Faculty is also an Employee and has areas of expertise (Courses)
class Faculty(Employee):
    def __init__(self, name: str):
        super().__init__(name)
        self.expertise: List[Course] = []        # List of courses they can teach

    def add_expertise(self, course):
        self.expertise.append(course)            # Add a course to expertise

# RegularFaculty is a Faculty who belongs to a department
class RegularFaculty(Faculty):
    def __init__(self, name: str, department: Department):
        super().__init__(name)
        self.department = department
        department.add_faculty(self)             # Automatically add them to the department

# VisitingFaculty is a Faculty who comes for a specific event
class VisitingFaculty(Faculty):
    def __init__(self, name: str, event: str):
        super().__init__(name)
        self.event = event                       # Event they are visiting for

# ExternalExaminer is a person from outside who comes for an exam event
class ExternalExaminer(Person):
    def __init__(self, name: str, event: str):
        super().__init__(name)
        self.event = event

# Student is a Person who enrolls in courses
class Student(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.courses: List[Course] = []          # List of courses student is enrolled in

    def enroll(self, course: Course):
        self.courses.append(course)              # Add course to student
        course.enroll_student(self)              # Add student to course

# ---------- USER INTERACTION SECTION ----------

inst_name = input("Enter the name of the Institution: ")
inst = Institution(inst_name)  # Create the Institution object

num_departments = int(input("How many departments? "))
for i in range(num_departments):
    dept_name = input("Enter department name: ")
    dept = Department(dept_name)
    inst.add_department(dept)
    
    num_courses = int(input("  How many courses in this department? "))
    for i in range(num_courses):
        course_name = input("    Enter course title: ")
        course = Course(course_name)
        dept.add_course(course)  # Add course to department

    num_faculty = int(input("  How many regular faculties in this department? "))
    for i in range(num_faculty):
        faculty_name = input("    Enter faculty name: ")
        faculty = RegularFaculty(faculty_name, dept)
        inst.add_employee(faculty)  # Add faculty to employees of institution

        exp_courses = input("    Enter course titles (comma separated) the faculty is expert in: ").split(',')
        for title in exp_courses:
            title = title.strip()  # Remove extra spaces
            for course in dept.courses:
                if course.title == title:
                    faculty.add_expertise(course)    # Add course to faculty’s expertise
                    course.assign_faculty(faculty)   # Add faculty to course

num_students = int(input("How many students? "))
students = []
for i in range(num_students):
    student_name = input("Enter student name: ")
    student = Student(student_name)
    students.append(student)

    enrolled_courses = input("  Enter courses to enroll (comma separated): ").split(',')
    for title in enrolled_courses:
        title = title.strip()
        for dept in inst.departments:
            for course in dept.courses:
                if course.title == title:
                    student.enroll(course)  # Enroll student in matching course

num_visiting = int(input("How many visiting faculties? "))
visiting_list = []
for _ in range(num_visiting):
    name = input("  Enter visiting faculty name: ")
    event = input("  Enter event name: ")
    vf = VisitingFaculty(name, event)
    visiting_list.append(vf)

    vf_courses = input("  Enter course titles (comma separated) they can teach: ").split(',')
    for title in vf_courses:
        title = title.strip()
        for dept in inst.departments:
            for course in dept.courses:
                if course.title == title:
                    vf.add_expertise(course)
                    course.assign_faculty(vf)

num_exam = int(input("How many external examiners? "))
exam_list = []
for _ in range(num_exam):
    name = input("  Enter examiner name: ")
    event = input("  Enter event name: ")
    examiner = ExternalExaminer(name, event)
    exam_list.append(examiner)

num_clerks = int(input("How many clerks? "))
for _ in range(num_clerks):
    name = input("  Enter clerk name: ")
    clerk = Clerk(name)
    inst.add_employee(clerk)

# ---------- OUTPUT SECTION ----------

print("\nInstitution: " + inst.name)

print("\nDepartments:")
for dept in inst.departments:
    print(" - " + dept.name)
    print("   Courses:")
    for course in dept.courses:
        print("     * " + course.title)
        print("       Faculties:")
        for faculty in course.faculties:
            print("         - " + faculty.name)
        print("       Enrolled Students:")
        for student in course.students:
            print("         - " + student.name)

print("\nEmployees on payroll:")
for emp in inst.employees:
    print(" - " + emp.name + " (" + emp.__class__.__name__ + ")")

print("\nVisitors:")
for vf in visiting_list:
    print(" - Visiting Faculty: " + vf.name + ", Event: " + vf.event)

for examiner in exam_list:
    print(" - External Examiner: " + examiner.name + ", Event: " + examiner.event)
