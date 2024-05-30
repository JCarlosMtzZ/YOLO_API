-- Inserting sample fruit data into the product table
INSERT INTO product (code, name, unitPrice) VALUES 
('FR001', 'Apple', 0.99),
('FR002', 'Banana', 0.59),
('DR003', 'Beer', 3.99),
('VE004', 'Bell pepper', 1.29),
('CE005', 'Bread', 2.49),
('VE006', 'Broccoli', 1.79),
('VE007', 'Cabbage', 1.49),
('FR008', 'Cantaloupe', 2.99),
('VE009', 'Carrot', 0.89),
('DA010', 'Cheese', 4.99),
('FR011', 'Coconut', 2.99),
('SN012', 'Cookie', 0.99),
('VE013', 'Cucumber', 0.79),
('SN014', 'Doughnut', 1.29),
('AO015', 'Egg', 0.25),
('FR016', 'Grape', 2.99),
('FR017', 'Lemon', 0.79),
('FR018', 'Mango', 1.99),
('DA019', 'Milk', 2.29),
('FR020', 'Orange', 0.89),
('FR021', 'Peach', 1.49),
('FR022', 'Pear', 1.29),
('FR023', 'Pineapple', 2.99),
('FR024', 'Pomegranate', 2.49),
('VE025', 'Potato', 0.49),
('VE026', 'Radish', 0.69),
('SN027', 'Snack', 1.99),
('FR028', 'Strawberry', 3.49),
('VE029', 'Tomato', 0.99),
('FR030', 'Watermelon', 3.99),
('DR031', 'Wine', 9.99),
('VE032', 'Zucchini', 1.19);

-- Inserting sample discount data into the discount table
INSERT INTO discount (name, amount, startDate, endDate) VALUES 
('10% Off Fruits', 0.10, '2024-05-23', '2024-06-30'),
('15% Off Vegetables', 0.15, '2024-05-23', '2024-06-30'),
('20% Off Dairy Products', 0.20, '2024-05-23', '2024-06-30'),
('Wine Lovers', 0.25, '2024-05-23', '2024-06-30');

-- Inserting sample data into the productDiscount table
INSERT INTO productDiscount (productCode, discountId) VALUES 
('FR001', 1), -- Apple
('FR002', 1), -- Banana
('FR008', 1), -- Cantaloupe
('FR011', 1), -- Coconut
('FR016', 1), -- Grape
('FR017', 1), -- Lemon
('FR018', 1), -- Mango
('FR020', 1), -- Orange
('FR021', 1), -- Peach
('FR022', 1), -- Pear
('FR023', 1), -- Pineapple
('FR024', 1), -- Pomegranate
('FR028', 1), -- Strawberry
('FR030', 1), -- Watermelon
('VE004', 2), -- Bell pepper
('VE006', 2), -- Broccoli
('VE007', 2), -- Cabbage
('VE009', 2), -- Carrot
('VE013', 2), -- Cucumber
('VE025', 2), -- Potato
('VE026', 2), -- Radish
('VE029', 2), -- Tomato
('DA010', 3), -- Cheese
('DA019', 3), -- Milk
('DR031', 4); -- Wine