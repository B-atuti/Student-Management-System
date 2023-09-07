# basic_reporting.py
import click
from student_management.database import Session
from student_management.models import Student, Course  

@click.command()
def student_report():
    """Generate a report of all students."""
    session = Session()
    students = session.query(Student).all()
    session.close()

    click.echo("Student Report:")
    for student in students:
        click.echo(f"ID: {student.id}, Name: {student.name}, Contact Info: {student.contact_info}")

if __name__ == '__main__':
    student_report()
