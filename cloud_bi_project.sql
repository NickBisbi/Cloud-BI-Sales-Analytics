-- 1. Δημιουργία της Βάσης
CREATE DATABASE IF NOT EXISTS cloud_bi_project;
USE cloud_bi_project;

-- 2. Δημιουργία Πινάκων
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    country VARCHAR(50),
    registration_date DATE
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    unit_price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    total_sales DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- 3. Εισαγωγή Δεδομένων (Seeding)
INSERT INTO Customers (customer_id, first_name, last_name, country, registration_date) VALUES
(1, 'Γιώργος', 'Παπαδόπουλος', 'Greece', '2023-01-15'),
(2, 'Maria', 'Garcia', 'Spain', '2023-02-20'),
(3, 'John', 'Smith', 'USA', '2023-03-05'),
(4, 'Ελένη', 'Νικολάου', 'Greece', '2023-04-10'),
(5, 'Hans', 'Mueller', 'Germany', '2023-05-12');

INSERT INTO Products (product_id, product_name, category, unit_price) VALUES
(101, 'Smartphone X', 'Electronics', 699.99),
(102, 'Laptop Pro', 'Electronics', 1299.50),
(103, 'Running Shoes', 'Clothing', 59.90),
(104, 'Coffee Maker', 'Home', 45.00),
(105, 'Bluetooth Headphones', 'Electronics', 89.99);

INSERT INTO Orders (order_id, customer_id, product_id, order_date, quantity, total_sales) VALUES
(1001, 1, 101, '2023-06-01', 1, 699.99),
(1002, 1, 105, '2023-06-02', 2, 179.98),
(1003, 2, 103, '2023-06-05', 1, 59.90),
(1004, 3, 102, '2023-07-01', 1, 1299.50),
(1005, 4, 104, '2023-07-10', 1, 45.00),
(1006, 5, 101, '2023-07-15', 1, 699.99),
(1007, 2, 101, '2023-08-01', 1, 699.99),
(1008, 4, 103, '2023-08-05', 2, 119.80);