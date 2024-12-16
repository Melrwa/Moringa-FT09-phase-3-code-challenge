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
    author = Author("John Doe")
    author3 = Author(name="Melki Doe")
    author4 = Author(name="Simeon Smith")
    
    # Add authors to the session and commit
    session.add(author3)
    session.add(author4)
    session.commit()

    # Create magazines
    magazine = Magazine("Tech Weekly",  category ="Technology")
    magazine3 = Magazine(name="People People", category="Politics")
    magazine4 = Magazine(name="Music Weekly", category="Music")
    
    # Add magazines to the session and commit
    session.add(magazine3)
    session.add(magazine4)
    session.commit()

    # Create articles with content
    article3 = Article(
        author=author3, 
        magazine=magazine3, 
        title="Just in politics", 
        content="This is a breaking news article on politics."
    )
    article4 = Article(
        author=author4, 
        magazine=magazine4, 
        title="Lately in music", 
        content="This is a recent update on the music industry."
    )
    
    # Add articles to the session and commit
    session.add(article3)
    session.add(article4)
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
