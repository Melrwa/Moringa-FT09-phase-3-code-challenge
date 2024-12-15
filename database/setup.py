

# database/setup.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base for declarative models
Base = declarative_base()

# Define the engine (adjust the database URI accordingly)
engine = create_engine('sqlite:///magazines.db')  # Replace with your actual database URI

# Create tables if they don't exist
def create_tables():
    Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

