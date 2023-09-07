# import unittest
# from click.testing import CliRunner
# from student_management.cli import add_student

# class TestCLIStudentManagement(unittest.TestCase):
#     def setUp(self):
#         self.runner = CliRunner()

#     def test_add_student_command(self):
#         result = self.runner.invoke(add_student, ["--name", "Alice", "--contact_info", "alice@example.com"])
#         self.assertEqual(result.exit_code, 0)  # Check if the command exits successfully

#         # Check if the command output contains a success message
#         self.assertIn("Student Alice added successfully.", result.output)
