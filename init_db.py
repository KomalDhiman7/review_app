from db import get_db

db = get_db()
cursor = db.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE,
    auth_token TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Places table
cursor.execute("""
CREATE TABLE IF NOT EXISTS places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    UNIQUE(name, address)
)
""")

# Reviews table
cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    text TEXT,
    user_id INTEGER NOT NULL,
    place_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, place_id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(place_id) REFERENCES places(id)
)
""")

db.commit()
db.close()

print("Database initialized successfully")
