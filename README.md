# Moringa FT09 Phase 3 Code Challenge

This project is part of the Moringa FT09 Phase 3 challenge, where we implement a Magazine system with relationships between Authors, Articles, and Magazines using SQLAlchemy. The project demonstrates how to use SQLAlchemy ORM to manage relationships in a database and perform basic CRUD operations.

## Project Structure

- `app.py`: The main script that sets up the database, creates tables, and performs operations like adding authors, magazines, and articles. It also demonstrates querying and printing data.
- `models/author.py`: Defines the `Author` class with properties and relationships to the `Article` model.
- `models/magazine.py`: Defines the `Magazine` class with properties and relationships to the `Article` model.
- `models/article.py`: Defines the `Article` class, including relationships to both `Author` and `Magazine`.
- `database/setup.py`: Contains the database setup, including engine, session creation, and table creation.

## Setup

### Requirements

- Python 3.x
- SQLAlchemy
- SQLite (or any other preferred SQL database)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-repository-url.git
    cd Moringa-FT09-phase-3-code-challenge
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Unix/Linux
    venv\Scripts\activate  # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python3 app.py
    ```

## Features

- **CRUD Operations**: The project demonstrates basic CRUD operations with `Author`, `Magazine`, and `Article` models.
- **Relationships**:
  - One-to-many relationship between `Author` and `Article`.
  - Many-to-many relationship between `Magazine` and `Author` through `Article`.
- **Database Setup**: The project uses SQLAlchemy to set up tables and manage relationships between them.

## Example Output

When you run `app.py`, it will:

- Create authors and magazines.
- Add articles linked to the authors and magazines.
- Query and print data such as:
  - Magazine name and category.
  - List of contributors (authors).
  - List of article titles associated with the magazine.

Example output:

