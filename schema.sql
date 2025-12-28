CREATE DATABASE IF NOT EXISTS review_app;
USE review_app;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    auth_token VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE places (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Ensures that the same place (name + address) cannot be duplicated
    -- Same name with different address is allowed
    UNIQUE KEY unique_place (name, address)
);


CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Rating between 1 and 5
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),

    -- Optional review text
    text TEXT,

    -- Foreign key to users table
    user_id INT NOT NULL,

    -- Foreign key to places table
    place_id INT NOT NULL,

    -- Time when the review was created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- A user can review a place only once
    UNIQUE KEY unique_user_place (user_id, place_id),

    -- Foreign key constraints
    CONSTRAINT fk_review_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_review_place
        FOREIGN KEY (place_id)
        REFERENCES places(id)
        ON DELETE CASCADE
);


