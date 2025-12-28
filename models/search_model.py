from db import get_db

def search_places(search_name, min_rating):
    """
    Search places by name (full or partial) and minimum average rating.
    Exact name matches are shown first, then partial matches.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT 
            p.id,
            p.name,
            AVG(r.rating) as avg_rating
        FROM places p
        JOIN reviews r ON p.id = r.place_id
        WHERE p.name LIKE ?
        GROUP BY p.id
        HAVING avg_rating >= ?
        ORDER BY
            CASE WHEN p.name = ? THEN 0 ELSE 1 END,
            p.name ASC
        """,
        (f"%{search_name}%", min_rating, search_name)
    )

    rows = cursor.fetchall()
    db.close()

    return [
        {
            "place_id": row["id"],
            "place_name": row["name"],
            "average_rating": round(row["avg_rating"], 2)
        }
        for row in rows
    ]
