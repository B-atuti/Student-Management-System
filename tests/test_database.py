# import unittest
# from student_management.database import Session
# from student_management.models import Student

# class TestDatabaseOperations(unittest.TestCase):
#     def test_insert_student(self):
#         session = Session()
#         student = Student(name="John Doe", contact_info="john@example.com")
#         session.add(student)
#         session.commit()

#         # Check if the student was inserted correctly
#         retrieved_student = session.query(Student).filter_by(name="John Doe").first()
#         self.assertIsNotNone(retrieved_student)
#         self.assertEqual(retrieved_student.contact_info, "john@example.com")

#         session.close()
