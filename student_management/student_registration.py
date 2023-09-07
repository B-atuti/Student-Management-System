# import click
# from student_management.database import Session
# from .models import Student

# @click.command()
# @click.option('--name', prompt='Enter student name', required=True)
# @click.option('--contact_info', prompt='Enter contact information')
# def add_student(name, contact_info):
#     """Add a new student."""
#     session = Session()
#     student = Student(name=name, contact_info=contact_info)
#     session.add(student)
#     session.commit()
#     session.close()
#     click.echo(f"Student {name} added successfully.")

# @click.command
# @click.option('--student_id', prompt='Enter student ID to delete', required=True, type=int)
# def delete_student(student_id):
#     """Delete a student by ID"""
#     session = Session()
#     student = session.query(Student).get(student_id)

#     if student:
#         student.delete(session)
#         session.commit()
#         click.echo(f"Student with ID {student_id} has been deleted.")
#     else:
#         click.echo(f"Student with ID {student_id} not found.")

# if __name__ == '__main__':
#     add_student()
