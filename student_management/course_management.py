# # course_management.py
# import click
# from student_management.database import Session
# from student_management.models import Course  

# @click.command()
# @click.option('--name', prompt='Enter course name', required=True)
# def create_course(name):
#     """Create a new course."""
#     session = Session()
#     course = Course(name=name)  
#     session.add(course)
#     session.commit()
#     session.close()
#     click.echo(f"Course {name} created successfully.")

# @click.command()
# @click.option('--course_id', prompt='Enter course ID to delete', required=True, type=int)
# def delete_course(course_id):
#     """Delete a course by ID."""
#     session = Session()
#     course = session.query(Course).get(course_id)

#     if course:
#         course.delete(session)
#         session.commit()
#         click.echo(f"Course with ID {course_id} has been deleted.")
#     else:
#         click.echo(f"Course with ID {course_id} not found.")

# if __name__ == '__main__':
#     create_course()
