# import sqlite3

# DATABASE_NAME = './database/magazine.db'

# def get_db_connection():
#     conn = sqlite3.connect(DATABASE_NAME)
#     conn.row_factory = sqlite3.Row
#     return conn


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///magazines.db"  # Use your actual DB connection URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

