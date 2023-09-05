
class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name

    
    def __str__(self):
        return f"{self.student_id}: {self.first_name} {self.last_name}"