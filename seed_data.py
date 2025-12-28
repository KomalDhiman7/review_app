import uuid
from db import get_db


def seed_users(db):
    """
    Inserts sample users into the users table.
    Uses INSERT OR IGNORE to avoid duplicate entries
    if the script is run multiple times.
    """
    users = [
        ("Komal", "9000000001"),
        ("Aman", "9000000002"),
        ("Riya", "9000000003")
    ]

    for name, phone in users:
        # Generate a unique auth token for each user
        token = str(uuid.uuid4())

        # Insert user into database
        db.execute(
            "INSERT OR IGNORE INTO users (name, phone, auth_token) VALUES (?, ?, ?)",
            (name, phone, token)
        )


def seed_places(db):
    """
    Inserts sample places into the places table.
    The (name, address) uniqueness constraint
    ensures no duplicate places are created.
    """
    places = [
        ("Cafe ABC", "Sector 18, Noida"),
        ("Burger Point", "Sector 62, Noida"),
        ("Pizza Hub", "Connaught Place, Delhi")
    ]

    for name, address in places:
        # Insert place if it does not already exist
        db.execute(
            "INSERT OR IGNORE INTO places (name, address) VALUES (?, ?)",
            (name, address)
        )


def seed_reviews(db):
    """
    Inserts sample reviews linking users and places.
    Demonstrates relationships between tables.
    """

    # Fetch all user IDs from database
    users = db.execute("SELECT id FROM users").fetchall()

    # Fetch all place IDs from database
    places = db.execute("SELECT id FROM places").fetchall()

    # Define sample reviews as (user_id, place_id, rating, text)
    reviews = [
        (users[0]["id"], places[0]["id"], 5, "Amazing place"),
        (users[1]["id"], places[0]["id"], 4, "Good coffee"),
        (users[2]["id"], places[1]["id"], 3, "Average taste"),
        (users[0]["id"], places[2]["id"], 4, "Nice ambience")
    ]

    for user_id, place_id, rating, text in reviews:
        # Insert review if user has not already reviewed the place
        db.execute(
            """
            INSERT OR IGNORE INTO reviews (user_id, place_id, rating, text)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, place_id, rating, text)
        )


def main():
    """
    Main entry point for the script.
    Opens a database connection and seeds all tables.
    """
    db = get_db()

    # Populate users, places, and reviews
    seed_users(db)
    seed_places(db)
    seed_reviews(db)

    # Commit all changes and close connection
    db.commit()
    db.close()

    print("Sample data inserted successfully")


# Execute script only when run directly
if __name__ == "__main__":
    main()
