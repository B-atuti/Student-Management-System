from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()


DATABASE_URI = "sqlite:///student_management.db"
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)



Base.metadata.create_all(engine)
