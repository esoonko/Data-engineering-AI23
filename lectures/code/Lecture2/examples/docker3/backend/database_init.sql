-- Create a sample table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);

-- Populate the table with sample data
INSERT INTO users (username) VALUES ('user1'), ('user2'), ('user3');
