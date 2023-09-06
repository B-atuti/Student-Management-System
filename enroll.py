# student_management/enrollment.py

class Enroll:
    def __init__(self, student, course, enrollment_date):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date

    def __str__(self):
        return f"{self.student} enrolled in {self.course} on {self.enrollment_date}"
