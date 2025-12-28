from db import get_db

def get_place_by_name_and_address(name, address):
    """
    Fetch a place using name and address.
    Used to check if place already exists.
    """
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM places WHERE name = %s AND address = %s",
        (name, address)
    )
    place = cursor.fetchone()

    cursor.close()
    db.close()
    return place


def create_place(name, address):
    """
    Create a new place entry in the database.
    This is called only if the place does not already exist.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO places (name, address) VALUES (%s, %s)",
        (name, address)
    )

    db.commit()
    cursor.close()
    db.close()


def get_place_by_id(place_id):
    """
    Fetch a place using its primary key.
    Used when showing place details.
    """
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM places WHERE id = %s",
        (place_id,)
    )
    place = cursor.fetchone()

    cursor.close()
    db.close()
    return place
