--\c daaccdb;

CREATE TABLE product (
    code VARCHAR(20) PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    unitPrice DECIMAL(10, 2) NOT NULL
);

CREATE TABLE discount (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    startDate TIMESTAMP NOT NULL,
    endDate TIMESTAMP NOT NULL
);

CREATE TABLE productDiscount (
    id SERIAL PRIMARY KEY,
    productCode VARCHAR(20) NOT NULL,
    discountId INT NOT NULL,
    FOREIGN KEY (productCode) REFERENCES product(code),
    FOREIGN KEY (discountId) REFERENCES discount(id)
);