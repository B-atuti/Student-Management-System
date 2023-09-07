# import click
# from student_management.database import Session
# from student_management.models import Base,enrollment_association

# @click.command()
# @click.option('--student_id', prompt='Enter student ID', required=True, type=int)
# @click.option('--course_id', prompt='Enter course ID', required=True, type=int)
# def enroll_student(student_id, course_id):
#     """Enroll a student in a course."""
#     session = Session()
    
#     enrollment = enrollment_association.insert().values(student_id=student_id, course_id=course_id)
#     session.execute(enrollment)
#     session.commit()
#     session.close()
#     click.echo(f"Student {student_id} enrolled in course {course_id}.")

# if __name__ == '__main__':
#     enroll_student()
