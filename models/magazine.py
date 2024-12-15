
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.setup import Base

class Magazine(Base):
    __tablename__ = 'magazines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(16), nullable=False)  # Internal name column
    _category = Column("category", String, nullable=False)  # Internal category column

    # Define relationship with Article
    articles = relationship('Article', back_populates='magazine')

    def __init__(self, name, category):
        self.name = name  # This will call the setter and initialize _name
        self.category = category  # This will call the setter and initialize _category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value  # Use _name to store the value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) < 1:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value  # Use _category to store the value

    def get_contributors(self):
        # Return authors who contributed to this magazine
        return [article.author for article in self.articles]

    def get_article_titles(self):
        # Return the titles of all articles in this magazine
        return [article.title for article in self.articles]

    def contributing_authors(self):
        authors = {}
        for article in self.articles:
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        return [author for author, count in authors.items() if count > 2]
