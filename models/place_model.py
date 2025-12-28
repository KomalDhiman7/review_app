from db import get_db

def get_place_by_name_and_address(name, address):
    """
    Fetch a place using name and address.
    Used to check if place already exists.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM places WHERE name = ? AND address = ?",
        (name, address)
    )
    row = cursor.fetchone()
    db.close()

    return dict(row) if row else None


def create_place(name, address):
    """
    Create a new place entry in the database.
    This is called only if the place does not already exist.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO places (name, address) VALUES (?, ?)",
        (name, address)
    )

    db.commit()
    place_id = cursor.lastrowid
    db.close()

    return place_id


def get_place_by_id(place_id):
    """
    Fetch a place using its primary key.
    Used when showing place details.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM places WHERE id = ?",
        (place_id,)
    )
    row = cursor.fetchone()
    db.close()

    return dict(row) if row else None
