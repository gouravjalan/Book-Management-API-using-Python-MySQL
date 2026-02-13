CREATE DATABASE book_manage;
USE book_manage;

CREATE TABLE IF NOT EXISTS book_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT NOT NULL,
    category_id INT NOT NULL,
    published_year INT,
    price DECIMAL(10,2)
);

INSERT INTO book_table(id,title,author_id,category_id,published_year,price) VALUES 
(1,'The Alchemist',020,12345,1988,300);

INSERT INTO book_table(id,title,author_id,category_id,published_year,price) VALUES
(2,' The Monk Who Sold His Ferrari',021,56789,1997,225.00),
(3,'Malgudi Days',022,13579,1982,350.00),
(4,'The White Tiger',023,02468,2008,450.35),
(5,'Atomic Habits',024,11111,2018,400.00),
(6,'Do Epic Shit',025,22222,2022,300.00),
(7,'Rich Dad Poor Dad',026,33333,2022,290),
(8,'Wings of Fire',027,44444,2000,200.00),
(9,'2 States',028,55555,2014,145.00),
(10,'12 Years',029,6666,2025,251.00);

ALTER TABLE book_table MODIFY price FLOAT;

UPDATE book_table SET author_id = author_id + 0;

UPDATE book_table SET id = 11 WHERE id = 15;
UPDATE book_table SET id = 12 WHERE id = 16;

ALTER TABLE book_table ADD CONSTRAINT unique_book UNIQUE (title, author_id);

DELETE FROM book_table WHERE id IN (11,12,13,14);

SELECT * FROM book_table;


