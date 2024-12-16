# app.py
from database.setup import engine, Session, create_tables
from models.author import Author
from models.magazine import Magazine
from models.article import Article

# Initialize the database and create tables
create_tables()
def main():
    # Initialize the database and create tables
    create_tables()



# Create a session
session = Session()

# Create some authors and magazines
author = Author(name="Jane Doe")
magazine = Magazine(name="Tech Monthly", category="Technology")

# Add authors and magazines to the session and commit
session.add(author)
session.add(magazine)
session.commit()

# Create articles
article1 = Article(author=author, magazine=magazine, title="The Future of AI")
article2 = Article(author=author, magazine=magazine, title="Quantum Computing: A Primer")
session.add(article1)
session.add(article2)
session.commit()

# Fetch the first magazine and its associated data
magazine = session.query(Magazine).first()

# Fetch authors who contributed to the magazine using the relationship
authors = magazine.get_contributors()  # Correct method name here

# Fetch article titles from the magazine using the relationship
titles = magazine.get_article_titles()

# Print out authors and article titles
print("Magazine Name:", magazine.name)  # Printing the magazine name
print("Magazine Category:", magazine.category)  # Printing the magazine category

# Print authors who contributed to the magazine
print("Contributors:")
for author in authors:
    print(f"- {author.name}")  # Printing each author's name

# Print article titles
print("Article Titles:")
for title in titles:
    print(f"- {title}")  # Printing each article's title

# Close the session
session.close()
