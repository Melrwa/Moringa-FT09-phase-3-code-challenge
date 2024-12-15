
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base
from models.author import Author
from models.magazine import Magazine

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String, nullable=False)  # Use _title as the internal column name
    author_id = Column(Integer, ForeignKey('authors.id'))
    magazine_id = Column(Integer, ForeignKey('magazines.id'))

    # Define relationship with Author and Magazine
    author = relationship('Author', back_populates='articles')
    magazine = relationship('Magazine', back_populates='articles')  # This line ensures back-population

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title  # This will call the setter

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value  # Use _title to store the value
