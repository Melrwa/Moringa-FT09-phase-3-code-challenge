# Moringa FT09 Phase 3 Code Challenge

This application manages authors, magazines, and articles using SQLAlchemy. Users can add new authors, magazines, and articles, view existing data, and query contributions. The application is designed with a relational database and provides basic CRUD functionality alongside advanced querying features.

## Project Structure

- **`app.py`**: The main script that provides an interactive menu to manage authors, magazines, and articles. It enables CRUD operations, querying, and displays specific relationships between models.
- **`models/author.py`**: Defines the `Author` class with properties and relationships to the `Article` model.
- **`models/magazine.py`**: Defines the `Magazine` class with properties and relationships to the `Article` model.
- **`models/article.py`**: Defines the `Article` class, including relationships to both `Author` and `Magazine`.
- **`database/setup.py`**: Contains the database setup, including engine creation and session management.

## Setup

### Requirements

- Python 3.x
- SQLAlchemy
- SQLite (default database)

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Melrwa/Moringa-FT09-phase-3-code-challenge.git
    cd Moringa-FT09-phase-3-code-challenge
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python3 app.py
    ```

## Features

- **Interactive Menu**: A user-friendly menu to perform actions such as creating, viewing, and querying data.
- **CRUD Operations**: Add and view authors, magazines, and articles.
- **Advanced Queries**:
  - View **all authors**.
  - View **all magazines**.
  - View **all articles** with details on authors and magazines.
  - View **articles written by a specific author**.
  - View **authors who contributed to a specific magazine**.
- **Relationships**:
  - One-to-many relationship between `Author` and `Article`.
  - Many-to-one relationship between `Article` and `Magazine`.

## Example Usage

When you run `app.py`, the following options are available:

1. **Create Entries**:
   - Create an Author
   - Create a Magazine
   - Create an Article (links an author to a magazine)

2. **View Data**:
   - Display all authors
   - Display all magazines
   - Display all articles with associated authors and magazines

3. **Advanced Queries**:
   - Display articles by a specific author (search by name or ID).
   - Display authors who have contributed to a specific magazine (search by name or ID).

### Sample Menu

===== Main Menu ===== 0: Create All (Author, Magazine, Article) 1: Create Author 2: Create Magazine 3: Create Article 4: Display All Authors 5: Display All Magazines 6: Display All Articles 7: Display Articles of a Specific Author 8: Display Authors Who Contributed to a Specific Magazine 00: Exit

### Example Input/Output

1. **Creating an Article**:
Enter the article title: Tech Trends Enter the article content: AI innovations in 2024 Choose an author (number): 1 Choose a magazine (number): 2 Article 'Tech Trends' created successfully.

2.**Viewing Articles**:

--- All Articles ---
 Title: "Tech Trends" | Author: John Doe | Magazine: Tech Weekly

3.**Advanced Query**: Articles by a specific author:
Enter the author's  ID: John Doe --- Articles by 'John Doe' --- Title: Tech Trends | Magazine: Tech Weekly

## License

This project is licensed under the [MIT License](https://github.com/Melrwa/Moringa-FT09-phase-3-code-challenge/blob/main/LICENSE).
