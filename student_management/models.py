# from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
# from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# enrollment_association = Table(
#     'enrollments',
#     Base.metadata,
#     Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
#     Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
# )

# class Student(Base):
#     __tablename__ = 'students'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     contact_info = Column(String(100))


#     courses = relationship('Course', secondary=enrollment_association, back_populates='students')

#     def __repr__(self):
#         return f"<Student(id={self.id}, name='{self.name}', contact_info='{self.contact_info}')>"
    
#     def delete(self, session):
#         session.delete(self)

# class Course(Base):
#     __tablename__ = 'courses'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)

#     students = relationship('Student', secondary=enrollment_association, back_populates='courses')

#     def __repr__(self):
#         return f"<Course(id={self.id}, name='{self.name}')>"
    
#     def delete(self, session):
#         session.delete(self)

# DATABASE_URI = "sqlite:///student_management.db"
# engine = create_engine(DATABASE_URI)

# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
