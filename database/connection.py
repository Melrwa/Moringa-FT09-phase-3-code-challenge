


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///magazines.db"  # Use your actual DB connection URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

