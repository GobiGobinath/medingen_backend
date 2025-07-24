
-- MySQL dump for Medingen backend task

DROP DATABASE IF EXISTS medingen;
CREATE DATABASE medingen;
USE medingen;

-- Products table
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    image_url TEXT
);

INSERT INTO products (name, image_url) VALUES
('Paracetamol Tablet', 'https://via.placeholder.com/150'),
('Ibuprofen Tablet', 'https://via.placeholder.com/150');

-- Salt Content table
CREATE TABLE salt_contents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    salt_name VARCHAR(100),
    quantity_mg FLOAT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO salt_contents (product_id, salt_name, quantity_mg) VALUES
(1, 'Paracetamol', 500),
(2, 'Ibuprofen', 400);

-- Reviews table
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    username VARCHAR(50),
    rating INT,
    comment TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO reviews (product_id, username, rating, comment) VALUES
(1, 'john_doe', 4, 'Works well for fever'),
(2, 'jane_smith', 5, 'Very effective painkiller');

-- Descriptions table
CREATE TABLE descriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    short_desc TEXT,
    full_desc TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO descriptions (product_id, short_desc, full_desc) VALUES
(1, 'Pain relief tablet', 'Paracetamol is used to treat mild to moderate pain and fever.'),
(2, 'Anti-inflammatory tablet', 'Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) used for pain relief, fever, and inflammation.');
