# Moringa FT09 Phase 3 Code Challenge

This application manages authors, magazines, and articles using SQLAlchemy. Users can add new authors, magazines, and articles, view existing data, and manage contributions. The application is designed with a relational database and provides basic CRUD functionality.

## Project Structure

- **`app.py`**: The main script that sets up the database, creates tables, and performs operations like adding authors, magazines, and articles. It also demonstrates querying and printing data.
- **`models/author.py`**: Defines the `Author` class with properties and relationships to the `Article` model.
- **`models/magazine.py`**: Defines the `Magazine` class with properties and relationships to the `Article` model.
- **`models/article.py`**: Defines the `Article` class, including relationships to both `Author` and `Magazine`.
- **`database/setup.py`**: Contains the database setup, including engine creation, session management, and table creation.
- **`database/connection.py`**: Handles the database connection and session creation.

## Setup

### Requirements

- Python 3.x
- SQLAlchemy
- SQLite (or any other SQL database)

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-repository-url.git
    cd Moringa-FT09-phase-3-code-challenge
    ```

2. Run the application:

    ```bash
    python3 app.py
    ```

## Features

- **CRUD Operations**: The project demonstrates basic Create, Read, and View operations for `Author`, `Magazine`, and `Article` models.
- **Relationships**:
  - One-to-many relationship between `Author` and `Article`.
  - Many-to-many relationship between `Magazine` and `Author` through `Article`.
- **Database Setup**: The project uses SQLAlchemy to set up tables and manage relationships between them.

## Example Usage

When you run `app.py`, it will prompt you to enter data for authors, magazines, and articles. For example:

1. **Creating an Author**: You can add a new author by providing their name.
2. **Creating a Magazine**: You can add a new magazine by specifying its name and category.
3. **Creating an Article**: You can create a new article by entering the article title, content, and linking it to an author and a magazine.

## License

This project is licensed under the [MIT License](https://github.com/Melrwa/Moringa-FT09-phase-3-code-challenge/blob/main/LICENSE).
