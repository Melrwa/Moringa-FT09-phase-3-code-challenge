# app.py
from database.setup import engine, Session, create_tables
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def main():
    # Create database tables
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

    # Create articles with content
    article1 = Article(
        author=author, 
        magazine=magazine, 
        title="The Future of AI", 
        content="An in-depth analysis of AI's future impact."
    )
    article2 = Article(
        author=author, 
        magazine=magazine, 
        title="Quantum Computing: A Primer", 
        content="An introductory guide to quantum computing concepts."
    )

    session.add(article1)
    session.add(article2)
    session.commit()

    # Fetch the first magazine and its associated data
    magazine = session.query(Magazine).first()

    # Fetch authors who contributed to the magazine using the relationship
    authors = magazine.get_contributors()

    # Fetch article titles from the magazine using the relationship
    titles = magazine.get_article_titles()

    # Print out authors and article titles
    print("Magazine Name:", magazine.name)
    print("Magazine Category:", magazine.category)

    # Print authors who contributed to the magazine
    print("Contributors:")
    for author in authors:
        print(f"- {author.name}")

    # Print article titles
    print("Article Titles:")
    for title in titles:
        print(f"- {title}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
