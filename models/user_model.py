from db import get_db

def create_user(name, phone, token):
    """
    Inserts a new user into the database.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO users (name, phone, auth_token) VALUES (%s, %s, %s)",
        (name, phone, token)
    )

    db.commit()
    cursor.close()
    db.close()

def get_user_by_phone(phone):
    """
    Fetches a user using phone number.
    Used to check uniqueness.
    """
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE phone = %s",
        (phone,)
    )
    user = cursor.fetchone()

    cursor.close()
    db.close()
    return user

def get_user_by_token(token):
    """
    Fetches user using auth token.
    Used for authentication middleware.
    """
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE auth_token = %s",
        (token,)
    )
    user = cursor.fetchone()

    cursor.close()
    db.close()
    return user
