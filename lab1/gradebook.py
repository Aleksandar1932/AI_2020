import math


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def __repr__(self):
        grades_string = str()
        for grade in self.grades:
            grades_string += "	" + repr(grade)

        return str("Student: %s\n" % self.name) + grades_string


class Grade:
    """Klasa za reprezentacija na kurs"""

    def __init__(self, course_name, course_grade):
        self.course_name = course_name
        self.course_grade = course_grade

    def __repr__(self) -> str:
        return str(f"{self.course_name}: {self.course_grade}\n")


if __name__ == "__main__":
    input_condition = True
    students = dict()
    while input_condition:
        line = input()
        if line == "end":
            input_condition = False
            break

        tokens = line.split(',')

        student_name = tokens[0] + " " + tokens[1]
        index = tokens[2]
        course_name = tokens[3]

        total_points = (int(tokens[4]) + int(tokens[5]) + int(tokens[6]))

        course_grade = 5  # definiranje inicijalno

        if total_points > 50:
            course_grade = math.ceil(total_points / 10)

        grade = Grade(course_name, course_grade)

        if index not in students:
            student = Student(student_name)
            student.add_grade(grade)
            students[index] = student

        elif index in students:
            students[index].add_grade(grade)

    for student in students.values():
        print(student)
