import sqlite3

DB_NAME = "review_app.db"

def get_db():
    """
    Creates and returns a SQLite database connection.
    Row factory is set to return dict-like rows.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
