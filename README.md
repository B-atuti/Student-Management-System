# Student Management System

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

[Project Description]: An efficient Command-Line-Interface (CLI) based Student Management System designed to streamline student data management and course administration in educational institutions.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Minimum Viable Product (MVP)](#minimum-viable-product-mvp)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Testing](#testing)
- [License](#license)

## Project Overview

The current manual student record management process in educational institutions is time-consuming, error-prone, and lacks a centralized system for easy access and management of student data. Administrative tasks are cumbersome, and data retrieval is challenging for both the student and the institution.

To address these challenges, we propose the development of a Command-Line-Interface (CLI) based Student Management System. This system provides a streamlined way for interacting and managing student-related information using the command line. It offers essential features for student data management and course administration.

## Features

- **Student Registration**: Enables administrators to add new students with essential details (name, contact information).
- **Course Management**: Allows administrators to create and manage courses.
- **Enrollment**: Allows students to enroll in available courses.
- **Basic Reporting**: Provides basic reports on student enrollment and course details.

## Technologies Used

- Programming Language: Python
- Database: SQLite (for simplicity)
- Object-Relational Mapping: SQLAlchemy
- Command-Line Interface: Click (for CLI command handling)
- Version Control: Git and GitHub
- Testing: Pytest

## Minimum Viable Product (MVP)

The Minimum Viable Product (MVP) of the Student Management System includes the following key features:

- Student Registration
- Course Management
- Enrollment
- Basic Reporting

## Getting Started

To get started with the Student Management System, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Initialize the database by running `python initialize_database.py`.

## Usage

You can interact with the system using the following CLI commands:

- `python main.py add_student`: Add a new student.
- `python main.py create_course`: Create a new course.
- `python main.py enroll_student`: Enroll a student in a course.
- `python main.py student_report`: Generate a report of all students.



## Testing

To run tests for the project, use the following command:

```shell
pytest
```
## Author & License

Authored by:

[Brian Atuti](https://github.com/B-atuti)

License

MIT License


