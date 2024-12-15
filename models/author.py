
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.setup import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(50), nullable=False)  # Internal name column

    # Define relationship with Article
    articles = relationship('Article', back_populates='author')

    def __init__(self, name):
        self.name = name  # This will call the setter and initialize _name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 50:
            raise ValueError("Name must be between 2 and 50 characters")
        self._name = value  # Use _name to store the value

