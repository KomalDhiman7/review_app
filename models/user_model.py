from db import get_db

def create_user(name, phone, token):
    """
    Inserts a new user into the database.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO users (name, phone, auth_token) VALUES (?, ?, ?)",
        (name, phone, token)
    )

    db.commit()
    db.close()


def get_user_by_phone(phone):
    """
    Fetches a user using phone number.
    Used to check uniqueness.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE phone = ?",
        (phone,)
    )

    row = cursor.fetchone()
    db.close()

    return dict(row) if row else None


def get_user_by_token(token):
    """
    Fetches user using auth token.
    Used for authentication.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE auth_token = ?",
        (token,)
    )

    row = cursor.fetchone()
    db.close()

    return dict(row) if row else None
