class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)


class Student:
    def __init__(self, student_id, name, department, gpa):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.remove_student(self)

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def show_info(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("GPA:", self.gpa)
        print("Courses:")
        for c in self.courses:
            print(c.code, c.name)


c1 = Course("AII003", "Software Engineering", 3)
c2 = Course("AII439", "Occupational Health And Safety", 2)
c3 = Course("MTH101", "Calculus", 4)

s1 = Student("20240816", "Efe", "Software Engineering", 2.1)

s1.enroll(c1)
s1.enroll(c2)
s1.enroll(c3)
s1.drop(c3)
s1.update_gpa(3)

print()
s1.show_info()
