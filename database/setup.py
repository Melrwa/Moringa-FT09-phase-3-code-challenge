# from .connection  import get_db_connection

# def create_tables():
#     conn = get_db_connection()
#     cursor = conn.cursor()
      
      
#     # Drop the old tables
#     cursor.execute('DROP TABLE IF EXISTS articles')
#     cursor.execute('DROP TABLE IF EXISTS magazines')
#     cursor.execute('DROP TABLE IF EXISTS authors')
    
#     # Authors Table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS authors (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL UNIQUE -- Must have a name and it must be unique
#         )
#     ''')
    
#     # Magazines Table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS magazines (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL, -- Must have a name and it must be unique
#             category TEXT NOT NULL CHECK(LENGTH(category) > 0) -- Must have a non-empty category
#         )
#     ''')
    
#     # Articles Table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS articles (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT NOT NULL CHECK(LENGTH(title) BETWEEN 5 AND 50), -- Title must be 5-50 characters
#             content TEXT NOT NULL, -- Article must have content
#             author_id INTEGER NOT NULL, -- Every article must be linked to an author
#             magazine_id INTEGER NOT NULL, -- Every article must be linked to a magazine
#             FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE, -- If an author is deleted, delete all their articles
#             FOREIGN KEY (magazine_id) REFERENCES magazines (id) ON DELETE CASCADE -- If a magazine is deleted, delete all its articles
#         )
#     ''')

#     conn.commit()
#     conn.close()

#     print("Tables recreated successfully")

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

