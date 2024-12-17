
# from sqlalchemy.orm import sessionmaker
# from database.setup import engine
# from models.author import Author
# from models.magazine import Magazine
# from models.article import Article

# Session = sessionmaker(bind=engine)
# session = Session()

# def main_menu():
#     while True:
#         print("\n===== Main Menu =====")
#         print("0: Create All (Author, Magazine, Article)")
#         print("1: Create Author")
#         print("2: Create Magazine")
#         print("3: Create Article")
#         print("00: Exit")
#         print("=====================")

#         choice = input("Enter your choice: ").strip()

#         if choice == "0":
#             create_all()
#         elif choice == "1":
#             create_author()
#         elif choice == "2":
#             create_magazine()
#         elif choice == "3":
#             create_article()
#         elif choice == "00":
#             print("Exiting program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# def create_author():
#     name = input("Enter the author's name: ").strip()
#     if name:
#         try:
#             author = Author(name=name)
#             session.add(author)
#             session.commit()
#             print(f"Author '{name}' created successfully.")
#         except ValueError as e:
#             print(f"Error: {e}")
#     else:
#         print("Author name cannot be empty.")

# def create_magazine():
#     name = input("Enter the magazine name: ").strip()
#     category = input("Enter the magazine category: ").strip()
#     if name and category:
#         try:
#             magazine = Magazine(name=name, category=category)
#             session.add(magazine)
#             session.commit()
#             print(f"Magazine '{name}' in category '{category}' created successfully.")
#         except ValueError as e:
#             print(f"Error: {e}")
#     else:
#         print("Magazine name and category cannot be empty.")

# def create_article():
#     print("\n--- Create Article ---")
#     title = input("Enter the article title: ").strip()
#     content = input("Enter the article content: ").strip()

#     print("\nAvailable Authors:")
#     authors = session.query(Author).all()
#     for index, author in enumerate(authors, start=1):
#         print(f"{index}. {author.name}")
#     author_choice = input("Choose an author (number): ").strip()

#     print("\nAvailable Magazines:")
#     magazines = session.query(Magazine).all()
#     for index, magazine in enumerate(magazines, start=1):
#         print(f"{index}. {magazine.name}")
#     magazine_choice = input("Choose a magazine (number): ").strip()

#     # Validate choices
#     try:
#         author = authors[int(author_choice) - 1]
#         magazine = magazines[int(magazine_choice) - 1]
#         article = Article(author=author, magazine=magazine, title=title, content=content)
#         session.add(article)
#         session.commit()
#         print(f"Article '{title}' created successfully under magazine '{magazine.name}' by author '{author.name}'.")
#     except (IndexError, ValueError):
#         print("Invalid selection. Article creation failed.")
#     except Exception as e:
#         print(f"Error: {e}")

# def create_all():
#     print("\n--- Create Author, Magazine, and Article ---")
#     create_author()
#     create_magazine()
#     create_article()

# if __name__ == "__main__":
#     main_menu()

from sqlalchemy.orm import sessionmaker
from database.setup import engine
from models.author import Author
from models.magazine import Magazine
from models.article import Article

# Initialize session
Session = sessionmaker(bind=engine)
session = Session()

# Main Menu Function
def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("0: Create All (Author, Magazine, Article)")
        print("1: Create Author")
        print("2: Create Magazine")
        print("3: Create Article")
        print("4: Display All Authors")
        print("5: Display All Magazines")
        print("6: Display All Articles")
        print("7: Display Articles of a Specific Author")
        print("8: Display Authors Who Contributed to a Specific Magazine")
        print("00: Exit")
        print("=====================")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            create_all()
        elif choice == "1":
            create_author()
        elif choice == "2":
            create_magazine()
        elif choice == "3":
            create_article()
        elif choice == "4":
            display_all_authors()
        elif choice == "5":
            display_all_magazines()
        elif choice == "6":
            display_all_articles()
        elif choice == "7":
            display_articles_by_author()
        elif choice == "8":
            display_authors_by_magazine()
        elif choice == "00":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to create an Author
def create_author():
    name = input("Enter the author's name: ").strip()
    if name:
        try:
            new_author = Author(name=name)
            session.add(new_author)
            session.commit()
            print(f"Author '{name}' created successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
    else:
        print("Author name cannot be empty.")

# Function to create a Magazine
def create_magazine():
    name = input("Enter the magazine name: ").strip()
    category = input("Enter the magazine category: ").strip()
    if name and category:
        try:
            new_magazine = Magazine(name=name, category=category)
            session.add(new_magazine)
            session.commit()
            print(f"Magazine '{name}' in category '{category}' created successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
    else:
        print("Magazine name and category cannot be empty.")

# Function to create an Article
def create_article():
    print("\n--- Create Article ---")
    title = input("Enter the article title: ").strip()
    content = input("Enter the article content: ").strip()

    # Fetch Authors
    authors = session.query(Author).all()
    if not authors:
        print("No authors found. Please create an author first.")
        return

    print("\nAvailable Authors:")
    for idx, author in enumerate(authors, start=1):
        print(f"{idx}. {author.name}")
    try:
        author_choice = int(input("Choose an author (number): ").strip())
        selected_author = authors[author_choice - 1]
    except (ValueError, IndexError):
        print("Invalid author selection.")
        return

    # Fetch Magazines
    magazines = session.query(Magazine).all()
    if not magazines:
        print("No magazines found. Please create a magazine first.")
        return

    print("\nAvailable Magazines:")
    for idx, magazine in enumerate(magazines, start=1):
        print(f"{idx}. {magazine.name}")
    try:
        magazine_choice = int(input("Choose a magazine (number): ").strip())
        selected_magazine = magazines[magazine_choice - 1]
    except (ValueError, IndexError):
        print("Invalid magazine selection.")
        return

    # Create Article
    if title and content:
        try:
            new_article = Article(
                title=title,
                content=content,
                author=selected_author,
                magazine=selected_magazine,
            )
            session.add(new_article)
            session.commit()
            print(f"Article '{title}' created successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
    else:
        print("Article title and content cannot be empty.")

# Display all Authors
def display_all_authors():
    authors = session.query(Author).all()
    if authors:
        print("\n--- All Authors ---")
        for author in authors:
            print(f"ID: {author.id} | Name: {author.name}")
    else:
        print("No authors found.")

# Display all Magazines
def display_all_magazines():
    magazines = session.query(Magazine).all()
    if magazines:
        print("\n--- All Magazines ---")
        for magazine in magazines:
            print(f"ID: {magazine.id} | Name: {magazine.name} | Category: {magazine.category}")
    else:
        print("No magazines found.")

# Display all Articles
def display_all_articles():
    articles = session.query(Article).all()
    if articles:
        print("\n--- All Articles ---")
        for article in articles:
            print(f"Title: {article.title} | Author: {article.author.name} | Magazine: {article.magazine.name}")
    else:
        print("No articles found.")

# Display Articles by a Specific Author
def display_articles_by_author():
    name_or_id = input("Enter the author's ID: ").strip()
    author = session.query(Author).filter((Author.id == name_or_id) | (Author.name == name_or_id)).first()
    if not author:
        print("Author not found.")
        return

    articles = session.query(Article).filter_by(author_id=author.id).all()
    if articles:
        print(f"\n--- Articles by '{author.name}' ---")
        for article in articles:
            print(f"Title: {article.title} | Magazine: {article.magazine.name}")
    else:
        print(f"No articles found for author '{author.name}'.")

# Display Authors Who Contributed to a Specific Magazine
def display_authors_by_magazine():
    name_or_id = input("Enter the magazine's  ID: ").strip()
    magazine = session.query(Magazine).filter((Magazine.id == name_or_id) | (Magazine.name == name_or_id)).first()
    if not magazine:
        print("Magazine not found.")
        return

    articles = session.query(Article).filter_by(magazine_id=magazine.id).all()
    authors = {article.author for article in articles}  # Use a set to avoid duplicates

    if authors:
        print(f"\n--- Authors Who Contributed to '{magazine.name}' ---")
        for author in authors:
            print(f"ID: {author.id} | Name: {author.name}")
    else:
        print(f"No authors have contributed to magazine '{magazine.name}'.")

# Function to create all (Author, Magazine, Article)
def create_all():
    print("\n--- Create Author, Magazine, and Article ---")
    create_author()
    create_magazine()
    create_article()

# Entry Point
if __name__ == "__main__":
    main_menu()
