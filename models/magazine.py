
# from database.connection import get_db_connection

# # Database connection setup
# conn = get_db_connection()
# cursor = conn.cursor()

# class Magazine:
#     def __init__(self, id=None, name=None, category=None):
#         """
#         Initialize a new Magazine object.
#         Either 'id' or 'name' and 'category' must be provided.
#         If 'name' and 'category' are provided, the Magazine is inserted into the database, and the ID is set.
#         If 'id' is provided, the Magazine is fetched from the database.
#         """
#         if id is not None:
#             if not isinstance(id, int) or id <= 0:
#                 raise ValueError('ID must be a positive integer.')
#             self._id = id
#             # Fetch magazine's details from the database
#             cursor.execute('SELECT name, category FROM magazines WHERE id = ?', (self._id,))
#             result = cursor.fetchone()
#             if result:
#                 self._name, self._category = result
#             else:
#                 raise ValueError(f"Magazine with id {self._id} not found in the database.")
        
#         elif name and category:
#             if not isinstance(name, str) or not (2 <= len(name) <= 16):
#                 raise ValueError("Name must be a string between 2-16 characters.")
#             if not isinstance(category, str) or len(category) == 0:
#                 raise ValueError("Category must be a non-empty string.")
            
#             # Check if the magazine already exists in the database
#             cursor.execute('SELECT id FROM magazines WHERE name = ? AND category = ?', (name, category))
#             result = cursor.fetchone()
#             if result:
#                 self._id = result[0]  # Magazine already exists, use the existing ID
#                 self._name = name
#                 self._category = category
#             else:
#                 # Insert a new magazine into the database
#                 cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
#                 conn.commit()
#                 self._id = cursor.lastrowid
#                 self._name = name
#                 self._category = category
#         else:
#             raise ValueError("Either 'id' or ('name' and 'category') must be provided to create a Magazine.")
        
#     @property
#     def name(self):
#         """ Return the magazine's name from the database. """
#         if not hasattr(self, '_name'):
#             cursor.execute('SELECT name FROM magazines WHERE id = ?', (self._id,))
#             result = cursor.fetchone()
#             if result:
#                 self._name = result[0]
#             else:
#                 raise ValueError("Magazine not found in the database.")
#         return self._name
    
#     @name.setter
#     def name(self, new_name):
#         """ Update the magazine's name in the database. """
#         if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
#             raise ValueError("Name must be a string between 2-16 characters.")
        
#         try:
#             cursor.execute('UPDATE magazines SET name = ? WHERE id = ?', (new_name, self._id))
#             conn.commit()
#             self._name = new_name  # Update the name in the object
#         except Exception as e:
#             print(f"Error updating name for magazine {self._id}: {e}")
    
#     @property
#     def category(self):
#         """ Return the magazine's category from the database. """
#         if not hasattr(self, '_category'):
#             cursor.execute('SELECT category FROM magazines WHERE id = ?', (self._id,))
#             result = cursor.fetchone()
#             if result:
#                 self._category = result[0]
#             else:
#                 raise ValueError("Magazine not found in the database.")
#         return self._category
    
#     @category.setter
#     def category(self, new_category):
#         """ Update the magazine's category in the database. """
#         if not isinstance(new_category, str) or len(new_category) == 0:
#             raise ValueError("Category must be a non-empty string.")
        
#         try:
#             cursor.execute('UPDATE magazines SET category = ? WHERE id = ?', (new_category, self._id))
#             conn.commit()
#             self._category = new_category  # Update the category in the object
#         except Exception as e:
#             print(f"Error updating category for magazine {self._id}: {e}")

#     @classmethod
#     def get(cls, magazine_id):
#         """ Retrieve a Magazine by its ID. """
#         if not isinstance(magazine_id, int) or magazine_id <= 0:
#             raise ValueError('ID must be a positive integer.')
        
#         cursor.execute('SELECT id, name, category FROM magazines WHERE id = ?', (magazine_id,))
#         result = cursor.fetchone()
#         if result:
#             return cls(id=result[0], name=result[1], category=result[2])  # Return Magazine object
#         else:
#             raise ValueError(f"Magazine with id {magazine_id} not found.")
    
#     def articles(self):
#         """ Retrieve all articles published in this magazine. """
#         try:
#             cursor.execute("""
#                 SELECT articles.title, articles.content, articles.author_id, articles.magazine_id
#                 FROM articles 
#                 WHERE articles.magazine_id = ?               
#             """, (self._id,))
#             return cursor.fetchall()
#         except Exception as e:
#             print(f"Error fetching articles for magazine {self._id}: {e}")
#             return []
    
#     def contributors(self):
#         """ Retrieve all authors who have contributed to this magazine. """
#         try:
#             cursor.execute("""
#                 SELECT DISTINCT authors.name
#                 FROM authors
#                 INNER JOIN articles ON articles.author_id = authors.id
#                 WHERE articles.magazine_id = ?
#             """, (self._id,))
#             results = cursor.fetchall()
#             from models.author import Author
#             return [Author(name=result[0]) for result in results]
#         except Exception as e:
#             print(f"Error fetching contributors for magazine {self._id}: {e}")
#             return []

#     def __repr__(self):
#         """ String representation of the Magazine. """
#         return f'<Magazine {self._name} of category {self._category}>'
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.setup import Base

class Magazine(Base):
    __tablename__ = 'magazines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(16), nullable=False)
    category = Column(String, nullable=False)

    # Define relationship with Article
    articles = relationship('Article', back_populates='magazine')

    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) < 1:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

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
