/*
CREATE DATABASE InventorySystem;
GO

USE InventorySystem;
GO


CREATE TABLE Products (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    purchase_price DECIMAL(10,2) NOT NULL,
    selling_price DECIMAL(10,2) NOT NULL,
    supplier VARCHAR(100) NOT NULL
);



CREATE TABLE Sales (
    sale_id INT IDENTITY(1,1) PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE DEFAULT GETDATE(),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);
*/


select * from Products;
select * from Sales;