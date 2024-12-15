from database.setup import create_tables, Session
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def main():
    # Create tables
    create_tables()

    # Create a session
    session = Session()

    # Create authors
    author1 = Author(name="Jane Doe")
    author2 = Author(name="John Smith")
    
    # Add authors to the session and commit
    session.add(author1)
    session.add(author2)
    session.commit()

    # Create magazines
    magazine1 = Magazine(name="Tech Monthly", category="Technology")
    magazine2 = Magazine(name="Science Weekly", category="Science")
    
    # Add magazines to the session and commit
    session.add(magazine1)
    session.add(magazine2)
    session.commit()

    # Create articles
    article1 = Article(author=author1, magazine=magazine1, title="The Future of AI")
    article2 = Article(author=author2, magazine=magazine2, title="Exploring Quantum Physics")
    
    # Add articles to the session and commit
    session.add(article1)
    session.add(article2)
    session.commit()

    # Fetch and display magazines and their contributors
    magazines = session.query(Magazine).all()
    for magazine in magazines:
        print(f"Magazine: {magazine.name} | Category: {magazine.category}")
        print("Contributors:")
        for author in magazine.get_contributors():
            print(f" - {author.name}")
        print("Article Titles:")
        for title in magazine.get_article_titles():
            print(f" - {title}")
        print()

    # Fetch and display authors and their articles
    authors = session.query(Author).all()
    for author in authors:
        print(f"Author: {author.name}")
        for article in author.articles:
            print(f" - {article.title} in {article.magazine.name}")
        print()

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
