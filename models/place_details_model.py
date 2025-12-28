from db import get_db

def get_place_details(place_id, current_user_id):
    """
    Fetch place details along with reviews.
    Current user's review appears first, others by newest.
    """
    db = get_db()
    cursor = db.cursor()

    # ---- PLACE INFO + AVG RATING ----
    cursor.execute(
        """
        SELECT 
            p.id,
            p.name,
            p.address,
            ROUND(AVG(r.rating), 2) as avg_rating
        FROM places p
        LEFT JOIN reviews r ON p.id = r.place_id
        WHERE p.id = ?
        GROUP BY p.id
        """,
        (place_id,)
    )

    place_row = cursor.fetchone()
    if not place_row:
        db.close()
        return None

    place = {
        "place_id": place_row["id"],
        "name": place_row["name"],
        "address": place_row["address"],
        "average_rating": place_row["avg_rating"]
    }

    # ---- REVIEWS ----
    cursor.execute(
        """
        SELECT 
            r.id,
            r.rating,
            r.text,
            r.created_at,
            u.name as user_name,
            r.user_id
        FROM reviews r
        JOIN users u ON r.user_id = u.id
        WHERE r.place_id = ?
        ORDER BY
            CASE WHEN r.user_id = ? THEN 0 ELSE 1 END,
            r.created_at DESC
        """,
        (place_id, current_user_id)
    )

    reviews_rows = cursor.fetchall()
    db.close()

    reviews = [
        {
            "review_id": row["id"],
            "rating": row["rating"],
            "text": row["text"],
            "created_at": row["created_at"],
            "user_name": row["user_name"],
            "is_current_user": row["user_id"] == current_user_id
        }
        for row in reviews_rows
    ]

    return {
        "place": place,
        "reviews": reviews
    }
