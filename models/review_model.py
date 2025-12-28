from db import get_db

def create_review(rating, text, user_id, place_id):
    """
    Creates a new review for a place by a user.
    Assumes the (user_id, place_id) pair is unique.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO reviews (rating, text, user_id, place_id)
        VALUES (?, ?, ?, ?)
        """,
        (rating, text, user_id, place_id)
    )

    db.commit()
    db.close()


def get_reviews_for_place(place_id, current_user_id):
    """
    Fetches all reviews for a given place.

    Ordering rules:
    1. Current user's review (if exists) comes first
    2. Remaining reviews sorted by newest first
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT r.*, u.name AS user_name
        FROM reviews r
        JOIN users u ON r.user_id = u.id
        WHERE r.place_id = ?
        ORDER BY
            CASE WHEN r.user_id = ? THEN 0 ELSE 1 END,
            r.created_at DESC
        """,
        (place_id, current_user_id)
    )

    rows = cursor.fetchall()
    db.close()

    return [dict(row) for row in rows]


def user_has_reviewed_place(user_id, place_id):
    """
    Checks if a user has already reviewed a specific place.
    Used to prevent duplicate reviews.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT id FROM reviews
        WHERE user_id = ? AND place_id = ?
        """,
        (user_id, place_id)
    )

    exists = cursor.fetchone() is not None
    db.close()
    return exists
