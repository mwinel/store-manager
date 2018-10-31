-- Create empty tables

CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(50), 
    username VARCHAR(20),
    email VARCHAR(20), 
    password VARCHAR(20), 
    admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY, 
    name VARCHAR(40), 
    description VARCHAR(200),
    quantity INTEGER, 
    price INTEGER
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id SERIAL PRIMARY KEY,
    name VARCHAR(40),
    quantity INTEGER,
    cost INTEGER
)
