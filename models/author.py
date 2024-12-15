
from database.connection import get_db_connection
from models.magazine import Magazine

# Database connection setup
conn = get_db_connection()
cursor = conn.cursor()

class Author:
    def __init__(self, id=None, name=None):
        """
        Initialize a new Author object. Either 'id' or 'name' must be provided.
        If 'name' is provided, the Author is inserted into the database, and the ID is set.
        If 'id' is provided, the Author is fetched from the database.
        """
        if id is not None:
            if not isinstance(id, int) or id <= 0:
                raise ValueError('ID must be a positive integer.')
            self._id = id
            # Fetch author's name from the database
            cursor.execute('SELECT name FROM authors WHERE id = ?', (self._id,))
            result = cursor.fetchone()
            if result:
                self._name = result[0]
            else:
                raise ValueError(f"Author with id {self._id} not found in the database.")
        
        elif name:
            if not isinstance(name, str) or len(name.strip()) == 0:
                raise ValueError("Name must be a non-empty string.")
            
            # Check if the author already exists in the database
            cursor.execute('SELECT id FROM authors WHERE name = ?', (name.strip(),))
            result = cursor.fetchone()
            if result:
                self._id = result[0]  # Author already exists, use the existing ID
                self._name = name.strip()
            else:
                # Insert a new author into the database
                cursor.execute('INSERT INTO authors (name) VALUES (?)', (name.strip(),))
                conn.commit()
                self._id = cursor.lastrowid
                self._name = name.strip()
        else:
            raise ValueError("Either 'id' or 'name' must be provided to create an Author.")
    
    @property
    def name(self):
        """
        Return the author's name. If it's not already loaded, fetch it from the database.
        """
        if not hasattr(self, '_name'):
            cursor.execute('SELECT name FROM authors WHERE id = ?', (self._id,))
            result = cursor.fetchone()
            if result:
                self._name = result[0]
            else:
                raise ValueError("Author not found in the database.")
        return self._name
    
    @name.setter
    def name(self, new_name):
        """
        Update the author's name in the database, if it's valid.
        """
        if not isinstance(new_name, str) or len(new_name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        
        try:
            cursor.execute('UPDATE authors SET name = ? WHERE id = ?', (new_name.strip(), self._id))
            conn.commit()
            self._name = new_name.strip()  # Update the name in the object
        except Exception as e:
            print(f"Error updating name for author {self._id}: {e}")
    
    @property
    def id(self):
        """ Return the author's ID. """
        return self._id
    
    @id.setter
    def id(self, new_id):
        """
        Update the author's ID, ensuring it is a valid positive integer.
        """
        if not isinstance(new_id, int) or new_id <= 0:
            raise ValueError('ID must be a positive integer.')
        self._id = new_id
    
    @classmethod
    def get(cls, author_id):
        """
        Retrieve an Author by their ID.
        """
        if not isinstance(author_id, int) or author_id <= 0:
            raise ValueError('ID must be a positive integer.')
        
        cursor.execute('SELECT id, name FROM authors WHERE id = ?', (author_id,))
        result = cursor.fetchone()
        if result:
            return cls(id=result[0], name=result[1])  # Return Author object
        else:
            raise ValueError(f"Author with id {author_id} not found.")
    
    def articles(self):
        """
        Retrieve all articles written by this author.
        """
        try:
            cursor.execute("""
                SELECT articles.title, articles.content, articles.author_id, articles.magazine_id
                FROM articles 
                WHERE articles.author_id = ?               
            """, (self._id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching articles for author {self._id}: {e}")
            return []
    
    def magazines(self):
        """
        Retrieve all magazines where this author has articles.
        """
        try:
            cursor.execute("""
                SELECT DISTINCT magazines.id, magazines.name, magazines.category
                FROM magazines
                INNER JOIN articles ON articles.magazine_id = magazines.id
                WHERE articles.author_id = ?
            """, (self._id,))
            results = cursor.fetchall()
            return [Magazine(id=result[0], name=result[1], category=result[2]) for result in results]
        except Exception as e:
            print(f"Error fetching magazines for author {self._id}: {e}")
            return []

    def __repr__(self):
        """
        String representation of the Author.
        """
        return f'<Author {self._name}>'
