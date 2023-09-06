# student_management/main.py
import click

@click.command()
def cli():
    click.echo("Welcome to the Student Management System CLI!")

if __name__ == "__main__":
    cli()
