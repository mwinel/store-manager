-- Create empty tables

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY, 
    username VARCHAR(20),
    email VARCHAR(20), 
    password VARCHAR(200), 
    admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY, 
    name VARCHAR(40), 
    description VARCHAR(200),
    quantity INTEGER, 
    price INTEGER,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id) 
    ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id SERIAL PRIMARY KEY,
    name VARCHAR(40),
    quantity INTEGER,
    price INTEGER,
    date TIMESTAMPTZ,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id) 
    ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS complete (
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products (product_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    sale_id INTEGER,
    FOREIGN KEY (sale_id) REFERENCES sales (sale_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    quantity INTEGER
);

INSERT INTO users (username, email, password, admin) 
SELECT * FROM (SELECT 'admin', 'admin@admin.com', 'admin', TRUE) 
AS tmp WHERE NOT EXISTS 
(SELECT username FROM users WHERE username = 'admin') LIMIT 1;
