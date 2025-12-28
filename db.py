import mysql.connector

def get_db():
    """
    Create and return a MySQL database connection.
    This function is reused across the project.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",      
        database="review_app"
    )